"""
Module for AGClient class.

AGClient class contians all the methods to interact with the AG server like creating a session, uploading results, etc.
It also contains methods to get the budget, privacy odometer, etc.

"""

import requests
import json
import warnings
import pandas as pd
from .magics.magics import AGMagic
from .enclave_client.oblv_client import get_oblv_client, oblv_client
from .config import config
from .models.models import AGServerInfo
from .utils.print_request_id import print_request_id
# optional imports
try:
    import onnx
    onnx_installed = True
except ImportError:
    onnx_installed = False
from io import BytesIO
import time
import base64
from .utils.loading_animation import _LoadingAnimation

def login(
    user_id: str,
    user_secret: str,
    competition: str = None,
    dataset: str = None,
):
    """
    Login to the AG server and get the client objects.

    Parameters:
        ag_client_id (str): The AG client ID.
        ag_client_secret (str): The AG client secret.
        competition (str, optional): The competition dataset ID.
        dataset (str, optional): The dataset ID.

    Returns:
        AGClient: The AGClient object.

    Raises:
        ConnectionError: If there is an error while creating the client.
    """
    try:
        return AGClient(user_id, user_secret, competition, dataset)
    except Exception as err:
        print(
            f"Login failed. Please verify the competition name and your credentials. If issue persists, contact support. Error: {str(err)}"
        )


class AGClient:
    """
    AGClient class to interact with the AG server for competitions as well as accessing datasets for functionalities like creating a session, uploading competition submissions, downloading metadata, etc.
    """

    oblv_enclave: oblv_client.Enclave
    session_id: str
    competition: str
    autoload_off = False
    session_timeout_time: int
    def __init__(self, ag_client_id, ag_client_secret, competition=None, dataset=None):
        """
        Initialize AGClient class and check for mock headers if MockClient.

        Parameters:
            ag_client_id (str): The AG client ID.
            ag_client_secret (str): The AG client secret.
            competition (str, optional): The competition dataset ID. Defaults to None.
            dataset (str, optional): The dataset ID. Defaults to None.

        Raises:
            ConnectionError: If there is an error while connecting to the server.
        """
        loading_messages = [
            "Fetching Platform Configuration Register (PCRs)...",
            "Retrieving attestation documents...",
            "Allocating antigranular sessions...",
            "Establishing secure and encrypted communication channels...",
            "Finalizing system resource allocation and readiness checks...",
            "Attesting the secure enclave..."
        ]
        try:
            animation = _LoadingAnimation(loading_messages)
            animation.start()
            self.competition = competition
            # Fetch latest PCRs from AG Server, and verify client version
            try:
                self._validate_server_info()
            except Exception as err:
                warnings.warn(f"Error while validating server info: {str(err)}")

            self.oblv_enclave = get_oblv_client(ag_client_id, ag_client_secret)
            self.headers = {}

            # Create an AG session
            self.connect(competition=competition, dataset=dataset)
            print(f"Connected to Antigranular server session id: {str(self.session_id)}, the session will time out if idle for {self.session_timeout_time} minutes")

            try:
                res = AGMagic.load_ag_magic()
            except Exception as ex:
                print(
                    "Error loading %%ag magic functions, you might not be able to use cell magics as intended: ",
                    str(ex),
                )

            AGMagic.load_oblv_client(self.oblv_enclave, self.session_id)
            print("🚀 Everything's set up and ready to roll!")
        finally:
            animation.stop()


    def _validate_server_info(self) -> None:
        """
        Get the PCR values to use from antigranular.com.
        PCRs are fed to the enclave client for PCR validation along with client version check.
        """
        try:
            res = requests.get(config.AG_SRV_INFO_URL)
        except Exception as err:
            warnings.warn(f"Error fetching server AG information: {str(err)}")
        else:
            if res.status_code != 200:
                warnings.warn(
                    f"Error while getting PCR values from antigranular.com status code: {res.status_code} message: {res.text}"
                )
            ag_server_info = AGServerInfo.parse_raw(res.text)

            # Update the PCR values from the response
            config.AG_PCRS = ag_server_info.AG_PCRs.dict()
            auto_load_off = ag_server_info.auto_load_off if ag_server_info.auto_load_off else []
            self.autoload_off = True if self.competition in auto_load_off else False
            self.session_timeout_time = ag_server_info.session_timeout_time if ag_server_info.session_timeout_time else 25
            from . import __version__

            if __version__ not in ag_server_info.supported_clients:
                warnings.warn(
                    f"Antigranular client version {__version__} not in supported clients list shared by the server, please update antigranular client to the latest version."
                )

    def connect(self, dataset: str = "", competition: str = "") -> None:
        """
        Connect to the AG server and create a session.

        Parameters:
            dataset (str, optional): The dataset ID. Defaults to "".
            competition (str, optional): The competition dataset ID. Defaults to "".

        Raises:
            ConnectionError: If there is an error while connecting to the server.
        """
    
        if not (dataset or competition):
            raise ValueError("dataset name or competition name must be provided.")
        if competition and dataset:
            raise ValueError(
                "Both competition and dataset cannot be passed. Please pass only one of them."
            )
        try:
            if competition:
                res = self._exec(
                    "POST",
                    "/start-session",
                    headers=self.headers,
                    json={
                        "session_type": "competition",
                        "type_identifier": competition,
                    },
                )
            if dataset:
                res = self._exec(
                    "POST",
                    "/start-session",
                    headers=self.headers,
                    json={"session_type": "dataset", "type_identifier": dataset},
                )
        except Exception as err:
            raise ConnectionError(f"Error calling /start-session: {str(err)}")
        else:
            if res.status_code != 200:
                raise requests.exceptions.HTTPError(
                    print_request_id(f"Error while starting a new session in enclave status code: {res.status_code} message: {res.text}", res)
                )
            self.session_id = json.loads(res.text)["session_id"]
            if not self.autoload_off:
                dataset_names = json.loads(res.text)["dataset_names"]
                for name in dataset_names:
                    name_identifier = name.replace(" ", "_").lower()
                    self.__session_execute(f"{name_identifier}=load_dataset('{name}')")

    def interrupt_kernel(self) -> dict:
        """
        Interrupt the current session.

        Returns:
            dict: The interrupt kernel response.

        Raises:
            ConnectionError: If there is an error while calling /interrupt-kernel.
            requests.exceptions.HTTPError: If there is an error while fetching the interrupt kernel.
        """
        try:
            res = self._exec(
                "POST",
                "/sessions/interrupt-kernel",
                headers=self.headers,
                json={"session_id": self.session_id},
            )
        except Exception as e:
            raise ConnectionError(f"Error calling /terminate-session: {str(e)}")
        else:
            if res.status_code != 200:
                raise requests.exceptions.HTTPError(
                    print_request_id(f"Error while fetching the terminate-session, HTTP status code: {res.status_code}, message: {res.text}", res)
                )
            return json.loads(res.text)

    def terminate_session(self) -> dict:
        """
        Terminate the current session.

        Returns:
            dict: The terminate session response.

        Raises:
            ConnectionError: If there is an error while calling /terminate-session.
            requests.exceptions.HTTPError: If there is an error while fetching the terminate session.
        """
        try:
            res = self._exec(
                "POST",
                "/sessions/terminate-session",
                headers=self.headers,
                json={"session_id": self.session_id},
            )
        except Exception as e:
            raise ConnectionError(f"Error calling /terminate-session: {str(e)}")
        else:
            if res.status_code != 200:
                raise requests.exceptions.HTTPError(
                    print_request_id(f"Error while fetching the terminate-session, HTTP status code: {res.status_code}, message: {res.text}", res)
                )
            return json.loads(res.text)

    def privacy_odometer(self) -> dict:
        """
        Get the privacy odometer.

        Returns:
            dict: The privacy odometer.

        Raises:
            ConnectionError: If there is an error while calling /privacy_odometer.
            requests.exceptions.HTTPError: If there is an error while fetching the privacy odometer.
        """
        try:
            res = self._exec(
                "GET",
                "/sessions/privacy_odometer",
                params={"session_id": self.session_id},
                headers=self.headers,
            )
        except Exception as e:
            raise ConnectionError(f"Error calling /privacy_odometer: {str(e)}")
        else:
            if res.status_code != 200:
                raise requests.exceptions.HTTPError(
                    print_request_id(f"Error while fetching the privacy odometer, HTTP status code: {res.status_code}, message: {res.text}", res)
                )
            return json.loads(res.text)

    def submit_predictions(self, data) -> dict:
        """
        Submit predictions to the AG server.

        Parameters:
            data (pd.DataFrame): The predictions dataframe.

        Returns:
            dict: The submit predictions response.
        """
        try:
            if not isinstance(data, pd.DataFrame):
                raise ValueError("data must be a DataFrame")
            
            res = self._exec(
                "POST",
                "/sessions/submit_predictions",
                json={"session_id": self.session_id, "data": data.to_json()},
                headers=self.headers,
            )
        except Exception as e:
            raise ConnectionError(f"Error calling /submit_predictions: {str(e)}")
        else:
            if res.status_code != 200:
                if res.status_code == 500:
                    return print_request_id(res.text, res)
                raise requests.exceptions.HTTPError(
                    print_request_id(f"Error: {res.text}", res)
                )
            return json.loads(res.text)

    def __get_output(self) -> None:
        """
        Retrieves the code execution output from the Antigranular server.
        """
        count = 1
        return_value = None
        while True:
            if count > config.AG_EXEC_TIMEOUT:
                print("Error : AG execution timeout.")
                return_value = True
                break
            try:
                res = self._exec(
                    "GET",
                    "/sessions/output",
                    params={"session_id": self.session_id}
                )
            except Exception as err:
                raise ConnectionError(
                    f"Error during code execution on AG Server: {str(err)}"
                )
            if res.status_code != 200:
                raise HTTPError(
                    f"Error while requesting AG server for output, HTTP status code: {res.status_code}, message: {res.text}"
                )
            kernel_messages = json.loads(res.text)["output_list"]
            for message in kernel_messages:
                if message["msg_type"] == "status":
                    if message["content"]["execution_state"] == "idle":
                        return return_value
                elif message["msg_type"] == "stream":
                    if message["content"]["name"] == "stdout":
                        print(message["content"]["text"])
                        return_value = True
                    elif message["content"]["name"] == "stderr":
                        print(message["content"]["text"])
                        return_value = True

                elif message["msg_type"] == "error":
                    tb_str = ""
                    for tb in message["content"]["traceback"]:
                        tb_str += tb

                    print(tb_str)
                    return_value = True
                    return return_value
            time.sleep(1)
            count += 1

        return return_value
    
    def __session_execute(self, code) -> None:
        if not code:
            raise ValueError("Code must be provided.")
        try:
            res = self._exec(
                "POST",
                "/sessions/execute",
                headers=self.headers,
                json={"session_id": self.session_id, "code": code},
            )
        except Exception as err:
            raise ConnectionError(f"Error calling /sessions/execute: {str(err)}")
        else:
            if res.status_code != 200:
                raise requests.exceptions.HTTPError(
                    f"Error while executing the provided compute operation in the enclave status code: {res.status_code} message: {res.text}"
                )
            return self.__get_output()

    def __load(self, name, data_type: str, metadata: dict, categorical_metadata: dict, is_private: bool) -> None:
        if data_type == "model":
            code = f"{name} = load_model('{name}')"
        if data_type == "dataframe" or data_type == "series":
            code = f"{name} = load_dataframe('{name}', metadata={metadata}, categorical_metadata={categorical_metadata}, is_private={is_private}, data_type='{data_type}')"

        try:
            self.__session_execute(code)
        except Exception as e:
            raise ConnectionError(f"Error calling /sessions/execute: {str(e)}")


    def private_import(self, data=None, name: str = None, path=None, is_private=False, metadata={}, categorical_metadata={}) -> None:
        """
        Load a user provided model or dataset into the AG server.

        Parameters:
            name (str): The name to use for the model or dataset.
            data (onnx.ModelProto, pd.DataFrame): The data to load. Defaults to None.
            path (str, optional): The path to the model, the external data should be under the same directory of the model. Defaults to None.
            is_private (bool, optional): Whether the data is private. Defaults to False.
            metadata (dict, optional): The metadata for the dataset. Defaults to {}.
            categorical_metadata (dict, optional): The categorical metadata for the dataset. Defaults to {}.
        Returns:
            None
        """
        if (name is None) or (not isinstance(name, str) and not name.isidentifier()):
            raise ValueError("name must be a valid identifier")
        if not (data is None or path is None):
            raise ValueError("Both data and path cannot be provided, please provide only one of them")
        if isinstance(data, pd.DataFrame):
            res = self._exec(
                "POST",
                "/sessions/cache_data",
                headers=self.headers,
                json={"session_id": self.session_id, "data": base64.b64encode(data.to_csv(index=True).encode()).decode(), "name": name},
            )
            data_type = "dataframe"
        elif isinstance(data, pd.Series):
            res = self._exec(
                "POST",
                "/sessions/cache_data",
                headers=self.headers,
                json={"session_id": self.session_id, "data": base64.b64encode(data.to_csv(header=False).encode()).decode(), "name": name},
            )
            data_type = "series"
        elif onnx_installed and isinstance(data, onnx.ModelProto):
            try:
                onnx.checker.check_model(data)
                onnx_bytes_io = BytesIO()
                onnx_bytes_io.seek(0)
                onnx.save_model(data, onnx_bytes_io)
            except Exception as e:
                raise ValueError(f"Invalid ONNX model: {str(e)}")
            res = self._exec(
                "POST",
                "/sessions/cache_model",
                headers=self.headers,
                json={"session_id": self.session_id, "name": name, "model": base64.b64encode(onnx_bytes_io.getvalue()).decode()},
            )
            data_type = "model"
        elif path:
            if not onnx_installed:
                raise ValueError("ONNX is not installed, please install ONNX to use this feature")
            if not path.endswith(".onnx"):
                raise ValueError("Invalid model file format, only .onnx files are supported")
            try:
                onnx_model = onnx.load(path)
                onnx.checker.check_model(onnx_model)
            except Exception as e:
                raise ValueError(f"Invalid ONNX model: {str(e)}")
            res = self._exec(
                "POST",
                "/sessions/cache_model",
                headers=self.headers,
                json={"session_id": self.session_id, "name": name, "model": base64.b64encode(open(path, "rb").read()).decode()},
            )
            data_type = "model"
        else:
            raise ValueError("Either a DataFrame, ONNX model, or path must be provided")
        

        if res.status_code != 200:
            raise requests.exceptions.HTTPError(
                print_request_id(f"Error: {res.text}", res)
            )
        else:
            print(f"{data_type} cached to server, loading to kernel...")
            self.__load(name, data_type, metadata, categorical_metadata, is_private)


    # Use Oblv Client enclave to make HTTP requests
    def _exec(self, method, endpoint, data="", json={}, params={}, headers={}, files=None):
        """
        Execute an HTTP request using the Oblv Client enclave.

        Parameters:
            method (str): The HTTP method.
            endpoint (str): The endpoint URL.
            data (Any, optional): The request data. Defaults to "".
            json (Any, optional): The request JSON. Defaults to None.
            params (dict, optional): The request parameters. Defaults to None.
            headers (dict, optional): The request headers. Defaults to None.

        Returns:
            Response: The HTTP response.

        Raises:
            ValueError: If the method is not supported by the client.
        """
        url_endpoint = f"{self.oblv_enclave.url}:{self.oblv_enclave.port}{endpoint}"
        if method == "GET":
            r = self.oblv_enclave.get(
                url_endpoint,
                json=json,
                params=params,
                headers=headers,
            )
        elif method == "POST":
            r = self.oblv_enclave.post(
                url_endpoint, json=json, params=params, headers=headers, files=files
            )
        elif method == "PUT":
            r = self.oblv_enclave.put(
                url_endpoint, json=json, params=params, headers=headers
            )
        elif method == "DELETE":
            r = self.oblv_enclave.delete(
                url_endpoint, json=json, params=params, headers=headers
            )
        else:
            raise ValueError(f"{method} not supported by client")
        return r

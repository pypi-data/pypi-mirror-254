"""
Copyright Oblivious Software - Antigranular
Pydantic models for client side validations and serialization before making a request to AG Enclave Server
"""

from pydantic import BaseModel
from typing import List, Optional


class UserLogin(BaseModel):
    """
    Pydantic model for User
    """

    user_id: str
    user_secret: str


class PCRs(BaseModel):
    """
    Pydantic model for PCRs
    """

    PCR0: str
    PCR1: str
    PCR2: str


class AGServerInfo(BaseModel):
    """
    Pydantic model for AG Server Info containing PCRs, and supported client versions
    """

    AG_PCRs: PCRs
    supported_clients: List[str]
    auto_load_off: Optional[List[str]] = None
    session_timeout_time: Optional[int] = None
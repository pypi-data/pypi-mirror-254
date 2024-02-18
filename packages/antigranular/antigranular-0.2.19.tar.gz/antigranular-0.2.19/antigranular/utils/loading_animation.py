import time
import threading
import random
from IPython.display import display, HTML

class _LoadingAnimation:
    def __init__(self, messages):
        self.messages = messages
        self.running = False
        self.t = None
        self.spin_idx = 0
        self.output = display(HTML(''), display_id=True)
        self.current_message = random.choice(self.messages)

    def start(self):
        self.running = True
        self.t = threading.Thread(target=self.animate)
        self.t.start()

    def stop(self):
        self.running = False
        self.t.join()
        self.clear_animation()

    def clear_animation(self):
        self.output.update(HTML(''))
    
    def animate(self):
        spinner = ['|', '/', '-', '\\']
        while self.running:
            html_content = f"{self.current_message} {spinner[self.spin_idx % len(spinner)]}"
            self.output.update(HTML(html_content))
            time.sleep(0.05) # Spinner updates every 0.05 seconds (fast spin)
            self.spin_idx += 1
            if self.spin_idx % 20 == 0: # Message updates every 20 spinner updates (1 second)
                self.current_message = random.choice(self.messages)

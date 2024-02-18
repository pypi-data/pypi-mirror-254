from threading import Thread
from dataclasses import dataclass
import time

from .messages import printf

@dataclass
class Spinners:
    line_spinner = [r"|", "\\", "-", "/"]
    mark_spinner = ["#", "!", "?", "$", "&"]

class loadbar(object):
    def __init__(self, spinner: list[str], __str: str, speed=0.4, spinner_color = None) -> None:
        self.spinner = spinner
        self.text = __str
        self.is_stopped = False
        self.speed = speed
        self.spinner_color = spinner_color

    def spin(self):
        while not self.is_stopped: 
            for a in self.spinner:
                if self.spinner_color:
                    a = self.spinner_color + a + "\033[0m"

                printf("\r" + a, self.text, end="", flush=True)
                time.sleep(self.speed)

    def __enter__(self):
        Thread(target=self.spin).start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_stopped = True

import time

import pyperclip


class ClipboardExchange:
    def __init__(self):
        pass

    @staticmethod
    def fetch() -> str:
        time.sleep(0.1)
        return str(pyperclip.paste())

    @staticmethod
    def send(text: str):
        pyperclip.copy(text)
        time.sleep(0.1)

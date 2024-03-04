from pynput.keyboard import Controller

from autocorrect_ai.ai import LLM
from autocorrect_ai.clipboard import ClipboardExchange
from .shortcuts import KeyboardShortcuts


class KeyboardController(Controller):
    def __init__(self, shortcuts: KeyboardShortcuts, clipboard: ClipboardExchange):
        super().__init__()
        self.shortcuts = shortcuts
        self.clipboard = clipboard

    @staticmethod
    def modify_text(text: str):
        text = LLM.generate(text)
        return text

    def fix_selection(self):
        self.shortcuts.cut()
        text = self.clipboard.fetch()

        text = self.modify_text(text)

        self.clipboard.send(text)
        self.shortcuts.paste()

    def fix_current_line(self):
        self.shortcuts.select_current_line()
        self.fix_selection()

    def fix_all(self):
        self.shortcuts.select_all()
        self.fix_selection()

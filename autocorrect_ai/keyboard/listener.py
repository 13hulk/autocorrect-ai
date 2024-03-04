from pynput.keyboard import GlobalHotKeys, Key

from .controller import KeyboardController


class HotkeyListener:
    def __init__(self, keyboard_controller: KeyboardController):
        self.controller = keyboard_controller

    def run(self):
        with GlobalHotKeys(
            {
                str(Key.f8.value): self.controller.fix_all,
                str(Key.f9.value): self.controller.fix_selection,
                str(Key.f10.value): self.controller.fix_current_line,
            }
        ) as h:
            h.join()

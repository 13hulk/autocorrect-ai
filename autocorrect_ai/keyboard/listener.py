from pynput.keyboard import GlobalHotKeys, Key

from autocorrect_ai.autocorrect_ai import LOG

from .controller import KeyboardController


class HotkeyListener:
    def __init__(self, keyboard_controller: KeyboardController):
        self.controller = keyboard_controller

    def on_f8(self):
        LOG.info(f"{Key.f8} pressed. Fixing all..")
        self.controller.fix_all()

    def on_f9(self):
        LOG.info(f"{Key.f9} pressed. Fixing selection..")
        self.controller.fix_selection()

    def on_f10(self):
        LOG.info(f"{Key.f10} pressed. Fixing current line..")
        self.controller.fix_current_line()

    def run(self):
        with GlobalHotKeys(
            {
                str(Key.f8.value): self.on_f8,
                str(Key.f9.value): self.on_f9,
                str(Key.f10.value): self.on_f10,
            }
        ) as h:
            h.join()

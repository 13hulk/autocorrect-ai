from pynput.keyboard import Controller, Key


class KeyboardShortcuts(Controller):
    def __init__(self):
        super().__init__()

    def cut(self):
        # Copy: <cmd> + x
        with self.pressed(Key.cmd):
            self.tap("x")

    def copy(self):
        # Copy: <cmd> + c
        with self.pressed(Key.cmd):
            self.tap("c")

    def paste(self):
        # Paste: <cmd> + v
        with self.pressed(Key.cmd):
            self.tap("v")

    def select_all(self):
        # Select all: <cmd> + a
        with self.pressed(Key.cmd):
            self.tap("a")

    def select_current_line(self):
        # 1. Move to the end of the current line: <cmd> + <right>
        with self.pressed(Key.cmd):
            self.tap(Key.right)

        # 2. Select the current line: <cmd> + <shift> + <left>
        self.press(Key.cmd)
        self.press(Key.shift)
        self.press(Key.left)

        self.release(Key.left)
        self.release(Key.shift)
        self.release(Key.cmd)

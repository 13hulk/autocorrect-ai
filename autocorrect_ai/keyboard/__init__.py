from kit.proxy import ProxyObject, Sentinel

from .controller import KeyboardController
from .listener import HotkeyListener
from .shortcuts import KeyboardShortcuts

__all__ = [
    "SHORTCUTS",
    "CONTROLLER",
    "LISTENER",
    "init_shortcuts",
    "init_controller",
    "init_listener",
    "KeyboardShortcuts",
    "KeyboardController",
    "HotkeyListener",
]

_sentinel_keyboard_shortcuts = Sentinel()
SHORTCUTS: KeyboardShortcuts = ProxyObject(_sentinel_keyboard_shortcuts)

_sentinel_keyboard_controller = Sentinel()
CONTROLLER: KeyboardController = ProxyObject(_sentinel_keyboard_controller)

_sentinel_hotkeys_listener = Sentinel()
LISTENER: HotkeyListener = ProxyObject(_sentinel_hotkeys_listener)


def init_shortcuts():
    global _sentinel_keyboard_shortcuts

    _sentinel_keyboard_shortcuts.obj: KeyboardShortcuts = KeyboardShortcuts()


def init_controller():
    global _sentinel_keyboard_controller
    from autocorrect_ai.clipboard import CLIPBOARD

    _sentinel_keyboard_controller.obj: KeyboardController = KeyboardController(
        SHORTCUTS, CLIPBOARD
    )


def init_listener():
    global _sentinel_hotkeys_listener

    _sentinel_hotkeys_listener.obj: HotkeyListener = HotkeyListener(CONTROLLER)

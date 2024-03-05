from kit.proxy import ProxyObject, Sentinel

from .exchange import ClipboardExchange

__all__ = ["CLIPBOARD", "ClipboardExchange", "init_clipboard"]

_sentinel_clipboard = Sentinel()
CLIPBOARD: ClipboardExchange = ProxyObject(_sentinel_clipboard)


def init_clipboard():
    global _sentinel_clipboard

    _sentinel_clipboard.obj: ClipboardExchange = ClipboardExchange()

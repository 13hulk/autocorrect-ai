from logfire import Logfire

from kit.proxy import ProxyObject, Sentinel

_sentinel_logger = Sentinel()
LOG: Logfire = ProxyObject(_sentinel_logger)


def init_logger():
    global _sentinel_logger
    _sentinel_logger.obj: Logfire = Logfire()

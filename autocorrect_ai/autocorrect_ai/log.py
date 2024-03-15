from logfire import Logfire, configure

from kit.proxy import ProxyObject, Sentinel

_sentinel_logger = Sentinel()
LOG: Logfire = ProxyObject(_sentinel_logger)


def init_logger():
    global _sentinel_logger

    configure(
        project_name="typing-assistant",
        service_name="autocorrect-ai",
        service_version="0.1.0",
        show_summary=True,
    )
    _sentinel_logger.obj: Logfire = Logfire()
    print(LOG.config)

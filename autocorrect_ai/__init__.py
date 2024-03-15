from autocorrect_ai.autocorrect_ai import LOG


def create_app():
    init_modules()
    LOG.info("Initialized all modules")


def init_modules():
    from autocorrect_ai.ai import init_llm, init_templates
    from autocorrect_ai.autocorrect_ai import init_logger
    from autocorrect_ai.clipboard import init_clipboard
    from autocorrect_ai.keyboard import init_controller, init_listener, init_shortcuts

    # Instrumentation
    # 1. Logger
    init_logger()
    LOG.info("Initialized logger")

    # AI engine
    # 2. Templates
    init_templates()
    LOG.info("Initialized templates")

    # 3. Language model
    init_llm()
    LOG.info("Initialized language model")

    # Modules
    # 4. Clipboard
    init_clipboard()
    LOG.info("Initialized clipboard")

    # 5. Keyboard shortcuts
    init_shortcuts()
    LOG.info("Initialized keyboard shortcuts")

    # 6. Keyboard controller
    init_controller()
    LOG.info("Initialized keyboard controller")

    # 7. Keyboard listener
    init_listener()
    LOG.info("Initialized keyboard listener")


def start_listener():
    from autocorrect_ai.keyboard import LISTENER

    LOG.info("Starting listener..")
    LISTENER.run()

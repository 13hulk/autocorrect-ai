def create_app():
    init_modules()


def init_modules():
    from autocorrect_ai.ai import init_llm, init_templates
    from autocorrect_ai.autocorrect_ai import init_logger
    from autocorrect_ai.clipboard import init_clipboard
    from autocorrect_ai.keyboard import init_controller, init_listener, init_shortcuts

    # Instrumentation
    # 1. Logger
    init_logger()

    # AI engine
    # 2. Language model
    init_llm()

    # 3. Templates
    init_templates()

    # Modules
    # 4. Clipboard
    init_clipboard()

    # 5. Keyboard shortcuts
    init_shortcuts()

    # 6. Keyboard controller
    init_controller()

    # 7. Keyboard listener
    init_listener()


def start_listener():
    from autocorrect_ai.keyboard import LISTENER

    LISTENER.run()

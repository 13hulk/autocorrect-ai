def create_app():
    init_modules()


def init_modules():
    from autocorrect_ai.ai import init_llm, init_templates
    from autocorrect_ai.autocorrect_ai import init_logger
    from autocorrect_ai.clipboard import init_clipboard
    from autocorrect_ai.keyboard import init_controller, init_listener, init_shortcuts

    init_logger()
    init_clipboard()
    init_shortcuts()
    init_controller()
    init_listener()
    init_templates()
    init_llm()


def start_listener():
    from autocorrect_ai.keyboard import LISTENER

    LISTENER.run()

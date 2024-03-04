def create_app():
    init_modules()


def init_modules():
    from autocorrect_ai.clipboard import init_clipboard
    from autocorrect_ai.keyboard import init_shortcuts, init_controller, init_listener
    from autocorrect_ai.ai import init_templates, init_llm

    init_clipboard()
    init_shortcuts()
    init_controller()
    init_listener()
    init_templates()
    init_llm()


def start_listener():
    from autocorrect_ai.keyboard import LISTENER

    LISTENER.run()

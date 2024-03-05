import logfire

from autocorrect_ai import create_app, start_listener

create_app()

if __name__ == "__main__":
    logfire.info("Starting listener..")
    start_listener()

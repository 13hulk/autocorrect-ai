from fastapi import FastAPI


async def create_app(service: str, testing: bool = False) -> FastAPI:
    app = FastAPI()
    app.get("/")

    return app

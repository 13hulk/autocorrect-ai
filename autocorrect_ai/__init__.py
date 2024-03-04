from fastapi import FastAPI


async def create_app(service: str, testing: bool = False) -> FastAPI:
    app = FastAPI()

    await register_routers(app)

    return app


async def register_routers(app: FastAPI):
    from autocorrect_ai.api import health_router

    app.include_router(health_router)

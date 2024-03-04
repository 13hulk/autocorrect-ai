from fastapi import APIRouter

health_router = APIRouter(
    tags=["health"],
    responses={404: {"description": "not found"}},
)


@health_router.get("/api/health", tags=["health"])
async def health():
    return {"detail": "health check ok!"}


@health_router.get("/", tags=["health"])
async def root():
    return {"detail": "i am [g]root!"}

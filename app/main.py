import logging

from fastapi import FastAPI
import uvicorn

from app.api.hello import router as hello_router


logging.basicConfig(level=logging.INFO, format="%(message)s")

app = FastAPI(title="test-ws-fastapi")
app.include_router(hello_router)


def main() -> None:
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=3000,
        reload=True,
    )

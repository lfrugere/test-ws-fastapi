import logging

from fastapi import FastAPI

from app.api.hello import router as hello_router


logging.basicConfig(level=logging.INFO, format="%(message)s")

app = FastAPI(title="test-ws-fastapi")
app.include_router(hello_router)

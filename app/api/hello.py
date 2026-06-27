import logging

from fastapi import APIRouter, Depends, Request

from app.core.security import get_current_client_app


logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/hello/{name}")
def hello(
    name: str,
    request: Request,
    client_app: str = Depends(get_current_client_app),
) -> dict[str, str]:
    logger.info(
        "Client %s called %s %s",
        client_app,
        request.method,
        request.url.path,
    )

    return {
        "message": f"Hello {name}",
        "client_app": client_app,
    }

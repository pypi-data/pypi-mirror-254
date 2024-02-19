from pathlib import Path

from fastapi import APIRouter
from fastapi.logger import logger
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from chris import __version__ as package_version
from chris.app import logging_utilities

router = APIRouter()


class Status(BaseModel):
    status: str = "healthy"


class Version(BaseModel):
    version: str = "0.1.0"


@logging_utilities.log_context("get_status", tag="api")
@router.get(path="/", response_model=Status)
def get_status() -> JSONResponse:
    logger.info("GET app status")
    return JSONResponse(
        {
            "status": "healthy",
        }
    )


@logging_utilities.log_context("get_version", tag="api")
@router.get(path="/version", response_model=Version)
def get_version() -> JSONResponse:
    logger.info("GET app version")
    return JSONResponse(
        {
            "version": package_version,
        }
    )


@logging_utilities.log_context("get_index", tag="api")
@router.get(path="/index")
def get_index() -> HTMLResponse:
    logger.info("GET app index!")
    templates_dirpath = Path(__file__).parent.parent / "templates"
    index_filepath = templates_dirpath / "index.html"
    index_content = index_filepath.read_text()
    return HTMLResponse(content=index_content, status_code=200)

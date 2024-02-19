from fastapi import APIRouter
from fastapi.responses import JSONResponse

from chris.app import logging_utilities
from chris.datasets.fetch import fetch_dataset
from chris.datasets.datasets import Datasets

router = APIRouter()


@logging_utilities.log_context("get_archive", tag="api")
@router.get(path="/archive")
def get_archive() -> JSONResponse:
    """Get archive data."""
    return JSONResponse(fetch_dataset(Datasets.ARCHIVE))

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from chris.app import logging_utilities
from chris.datasets.fetch import fetch_dataset
from chris.datasets.datasets import Datasets

router = APIRouter()


@logging_utilities.log_context("get_recipes", tag="api")
@router.get(path="/recipes")
def get_recipes() -> JSONResponse:
    """Get recipe data."""
    return JSONResponse(fetch_dataset(Datasets.RECIPES))

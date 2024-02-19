from fastapi import APIRouter
from fastapi.responses import JSONResponse

from chris.app import logging_utilities
from chris.datasets.fetch import fetch_dataset
from chris.datasets.datasets import Datasets

router = APIRouter()


@logging_utilities.log_context("get_professional", tag="api")
@router.get(path="/professional")
def get_professional() -> JSONResponse:
    """Get professional data."""
    return JSONResponse(
        {
            "courses": fetch_dataset(Datasets.COURSES),
            "jobs": fetch_dataset(Datasets.JOBS),
        }
    )


@logging_utilities.log_context("get_professional_courses", tag="api")
@router.get(path="/professional/courses")
def get_professional_courses() -> JSONResponse:
    """Get college course data."""
    return JSONResponse(fetch_dataset(Datasets.COURSES))


@logging_utilities.log_context("get_professional_jobs", tag="api")
@router.get(path="/professional/jobs")
def get_professional_jobs() -> JSONResponse:
    """Get job data."""
    return JSONResponse(fetch_dataset(Datasets.JOBS))

from datetime import datetime
from typing import Any, Dict, List

from fastapi import APIRouter
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from chris.app import logging_utilities
from chris.datasets.fetch import fetch_dataset
from chris.datasets.datasets import Datasets

router = APIRouter()


class RequestModel(BaseModel):
    choices: List[List[bool]]
    feedback: str


@logging_utilities.log_context("get_surveys", tag="api")
@router.get(path="/surveys")
def get_surveys() -> JSONResponse:
    """Get survey data."""
    return JSONResponse(fetch_dataset(Datasets.SURVEYS))


@logging_utilities.log_context("post_survey_results", tag="api")
@router.post(path="/surveys/{survey_id}")
def post_survey_results(request: RequestModel, survey_id: str) -> JSONResponse:
    """Post a survey result."""
    surveys = fetch_dataset(Datasets.SURVEYS)
    # TODO: Check for invalid survey ID
    for survey in surveys:
        if survey["survey_id"] == survey_id:
            survey_name = survey["name"]
            logger.info(f'Survey "{survey_name}" ({survey_id}) submitted')
            _ = {
                "survey_id": survey_id,
                "created_date": datetime.now(),
                "response": request,
            }
            # db.insert_one(document)

            return JSONResponse({"message": f'Successfully submitted survey "{survey_name}"'})
    return JSONResponse({"message": f"Survey with ID {survey_id} not found"})


@logging_utilities.log_context("get_survey_results", tag="api")
@router.get(path="/surveys/results")
def get_survey_results() -> JSONResponse:
    """Get survey data."""
    # result_documents = list(db.find_all())
    result_documents: List[Dict[str, Any]] = []
    counts = {}
    for result_document in result_documents:
        survey_id = result_document["survey_id"]
        choices_array = [[int(v) for v in vs] for vs in result_document["response"]["choices"]]
        if survey_id not in counts:
            counts[survey_id] = [[0 for _ in xs] for xs in choices_array]

        for i in range(len(counts[survey_id])):
            for j in range(len(counts[survey_id][0])):
                counts[survey_id][i][j] += choices_array[i][j]
    surveys = fetch_dataset(Datasets.SURVEYS)
    survey_map = {survey["survey_id"]: survey for survey in surveys}
    return JSONResponse(_results_from_counts(counts, survey_map))


def _results_from_counts(counts: Dict[str, List[List[int]]], survey_map: Dict[str, Any]) -> List[Dict[str, Any]]:
    results = []
    for survey_id, survey_counts in counts.items():
        survey = survey_map[survey_id]
        survey_result_questions = []
        for question_counts, question in zip(survey_counts, survey["questions"]):
            question_counts_sum = sum(question_counts)
            question_frequencies = [c / question_counts_sum for c in question_counts]
            question_result_choices = []
            for option_number in range(len(question["options"])):
                question_result_choices.append(
                    {
                        "option": question["options"][option_number],
                        "frequency": float(question_frequencies[option_number]),
                        "count": float(question_counts[option_number]),
                    }
                )
            survey_result_questions.append(
                {
                    "question": question["text"],
                    "options": question_result_choices,
                }
            )
        results.append(
            {
                "survey_name": survey["name"],
                "questions": survey_result_questions,
            }
        )
    return results

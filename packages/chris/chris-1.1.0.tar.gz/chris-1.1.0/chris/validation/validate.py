"""Post validator."""

from jsonvl import Validator
from jsonvl.errors import JsonValidationError
from pathlib import Path
from chris.validation.constraints import MonotoneIncreaseConstraint

DATA_DIRPATH = Path(__file__).parent.parent / "datasets" / "data"
SCHEMAS_DIRPATH = Path(__file__).parent / "schemas"


def validate_all() -> None:
    """Validate all entities."""

    validator = Validator()
    validator.register_constraint(MonotoneIncreaseConstraint(), "array", "monotone_inc")
    schema_map = [
        ("books", "media/books.json", "books-schema.json"),
        ("courses", "professional/courses.json", "courses-schema.json"),
        ("hiking", "outdoor/hiking-routes.json", "hiking-routes-schema.json"),
        ("jobs", "professional/jobs.json", "jobs-schema.json"),
        ("posts", "blog/posts.json", "posts-schema.json"),
        ("projects", "projects/projects.json", "projects-schema.json"),
    ]
    for name, data_filename, schema_filename in schema_map:
        data_filepath = DATA_DIRPATH / data_filename
        schema_filepath = SCHEMAS_DIRPATH / schema_filename

        try:
            validator.validate_file(data_filepath, schema_filepath)
        except JsonValidationError as e:
            print(f"Validation failed: {name}")
            print(e)
        else:
            print(f"Validation succeeded: {name}")

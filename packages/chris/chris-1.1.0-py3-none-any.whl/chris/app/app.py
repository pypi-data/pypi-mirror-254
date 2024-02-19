"""Package web application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chris.app.routes import (
    archive_routes,
    info_routes,
    media_routes,
    outdoor_routes,
    post_routes,
    professional_routes,
    project_routes,
    recipe_routes,
    surveys_routes,
)

ALLOWED_ORIGINS = [
    "http://localhost:3001",
    "https://www.chrisgregory.me",
    "https://chrisgregory.me",
]

app = FastAPI()

app.include_router(archive_routes.router)
app.include_router(info_routes.router)
app.include_router(media_routes.router)
app.include_router(outdoor_routes.router)
app.include_router(post_routes.router)
app.include_router(professional_routes.router)
app.include_router(project_routes.router)
app.include_router(recipe_routes.router)
app.include_router(surveys_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

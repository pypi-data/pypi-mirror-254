"""Information for all package datasets."""

from chris.datasets.dataset_format import DatasetFormat
from chris.datasets.dataset_info import DatasetInfo


class Datasets:
    """Information for all package datasets."""

    # region blog

    PODCAST_EPISODES = DatasetInfo(
        "Podcast Episodes",
        "blog/podcast-episodes.json",
        DatasetFormat.JSON,
        "Podcast episodes.",
    )

    POSTS = DatasetInfo(
        "Posts",
        "blog/posts.json",
        DatasetFormat.JSON,
        "Blog posts.",
    )

    # endregion blog

    # region cooking

    RECIPES = DatasetInfo(
        "Recipes",
        "cooking/recipes.json",
        DatasetFormat.JSON,
        "Cooking recipes.",
    )

    # endregion cooking

    # region media

    MOVIES = DatasetInfo(
        "Movies",
        "media/movies.json",
        DatasetFormat.JSON,
        "Movies.",
    )

    PODCASTS = DatasetInfo(
        "Podcasts",
        "media/podcasts.json",
        DatasetFormat.JSON,
        "Podcasts.",
    )

    TV_SHOWS = DatasetInfo(
        "TV Shows",
        "media/tv-shows.json",
        DatasetFormat.JSON,
        "TV shows.",
    )

    YOUTUBE_CHANNELS = DatasetInfo(
        "YouTube Channels",
        "media/youtube-channels.json",
        DatasetFormat.JSON,
        "YouTube channels.",
    )

    BOOKS = DatasetInfo(
        "Books",
        "media/books.json",
        DatasetFormat.JSON,
        "Books.",
    )

    # endregion media

    # region outdoor

    CYCLING_ROUTES = DatasetInfo(
        "Cycling Routes",
        "outdoor/cycling-routes.json",
        DatasetFormat.JSON,
        "Cycling routes.",
    )

    HIKING_ROUTES = DatasetInfo(
        "Hiking Routes",
        "outdoor/hiking-routes.json",
        DatasetFormat.JSON,
        "Hiking routes.",
    )

    RUNNING_ROUTES = DatasetInfo(
        "Running Routes",
        "outdoor/running-routes.json",
        DatasetFormat.JSON,
        "Running routes.",
    )

    # endregion outdoor

    # region professional

    COURSES = DatasetInfo(
        "College Courses",
        "professional/courses.json",
        DatasetFormat.JSON,
        "College courses.",
    )

    JOBS = DatasetInfo(
        "Jobs",
        "professional/jobs.json",
        DatasetFormat.JSON,
        "Jobs.",
    )

    # endregion professional

    # region projects

    PROJECTS = DatasetInfo(
        "Projects",
        "projects/projects.json",
        DatasetFormat.JSON,
        "Software projects.",
    )

    # endregion projects

    # region archive

    ARCHIVE = DatasetInfo(
        "Archive",
        "archive/archive.json",
        DatasetFormat.JSON,
        "Personal website revision archive.",
    )

    # endregion archive

    # region surveys

    SURVEYS = DatasetInfo(
        "Surveys",
        "surveys/surveys.json",
        DatasetFormat.JSON,
        "Surveys.",
    )

    # endregion surveys

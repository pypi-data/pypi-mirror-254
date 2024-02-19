# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chris',
 'chris.app',
 'chris.app.routes',
 'chris.cli',
 'chris.datasets',
 'chris.utilities',
 'chris.validation',
 'chris.validation.constraints']

package_data = \
{'': ['*'],
 'chris.app': ['templates/*'],
 'chris.datasets': ['data/archive/*',
                    'data/blog/*',
                    'data/cooking/*',
                    'data/media/*',
                    'data/outdoor/*',
                    'data/professional/*',
                    'data/projects/*',
                    'data/surveys/*'],
 'chris.validation': ['schemas/*']}

install_requires = \
['click>=8.1.7,<9.0.0',
 'fastapi>=0.109.2,<0.110.0',
 'httpx>=0.26.0,<0.27.0',
 'jsonvl>=0.5.0,<0.6.0',
 'pandas>=2.2.0,<3.0.0',
 'pydantic>=2.6.0,<3.0.0',
 'uvicorn[standard]>=0.27.0,<0.28.0']

entry_points = \
{'console_scripts': ['cgme = chris.cli.main:cli']}

setup_kwargs = {
    'name': 'chris',
    'version': '1.1.0',
    'description': 'Personal website SDK',
    'long_description': '# Personal Website Backend\n\n## About\n\nThe `chris` Python package is the backend for the website [chrisgregory.me](http://www.chrisgregory.me)\n\n## Usage\n\n```bash\n# Install the chris package from PyPI\npip install chris\n\n# Start the local Flask server\ncgme app\n```\n\nThen open `localhost:8000` in a browser to check that you can access the API\n\n## Frontend\n\nDetails for running the frontend locally can be found in the [GitHub repo for the project](https://github.com/gregorybchris/personal-website)\n',
    'author': 'Chris Gregory',
    'author_email': 'christopher.b.gregory@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gregorybchris/personal-website',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lineage_aq']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0', 'networkx>=2.8.5,<3.0.0', 'requests>=2.31.0,<3.0.0']

entry_points = \
{'console_scripts': ['lineage = lineage_aq.__main__:main']}

setup_kwargs = {
    'name': 'lineage-aq',
    'version': '1.4.0',
    'description': 'Interactive command line interface to create and edit lineage of families.',
    'long_description': '# Lineage\n\nGenealogy management software  \nStores lineage of family. Interactive command line interface to create and edit lineage of families. \n\n\n### Lineage\nnoun:\nthe series of families that somebody comes from originally  \nवंश, वंशावली\n\n\n# Install\n###### Recommended (To install pipx click [here](https://github.com/pypa/pipx#install-pipx))\n```\npipx install lineage-aq\n```\n\n###### or\n```\npip install lineage-aq\n```\n\n#### Or upgrade by:\n```\npipx upgrade lineage-aq\n```\n###### or\n```\npip install --upgrade lineage-aq\n```\n# Usage\n\n### Execute:\n```\nlineage\n```\n\n\n# Install from source\nPoetry is required. For installation click [here](https://python-poetry.org/docs/#installation).\n\n   Download the source and install the dependencies by running:\n  \n   ``` \n   git clone https://github.com/aqdasak/Lineage.git\n   cd Lineage\n   poetry install\n   ```\n\n### Run\nIn the source folder containing pyproject.toml, run\n```\npoetry shell\nlineage\n```\n\n> For Python3.7 compatible version click [here](https://github.com/aqdasak/Lineage-py37)\n',
    'author': 'Aqdas Ahmad Khan',
    'author_email': 'aqdasak@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aqdasak/Lineage/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

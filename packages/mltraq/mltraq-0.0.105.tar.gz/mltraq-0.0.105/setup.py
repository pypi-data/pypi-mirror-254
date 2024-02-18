# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mltraq', 'mltraq.storage', 'mltraq.storage.serializers', 'mltraq.utils']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=2.2.0',
 'joblib>=1.3.2',
 'pandas>=1.5.3',
 'pyarrow>=10.0.0',
 'sqlalchemy>=2.0.0',
 'tqdm>=4.64.1']

extras_require = \
{'complete': ['scikit-learn>=1.1.3,<2.0.0',
              'dask[complete]>=2022.11.0,<2023.0.0',
              'psycopg[binary]>=3.1.17,<4.0.0'],
 'dask': ['dask[complete]>=2022.11.0,<2023.0.0'],
 'pgsql': ['psycopg[binary]>=3.1.17,<4.0.0']}

setup_kwargs = {
    'name': 'mltraq',
    'version': '0.0.105',
    'description': 'Design ML Experiments as State Monads with Persistence',
    'long_description': '<p align="center">\n<img width="33%" height="33%" src="https://mltraq.com/assets/img/logo-black.svg" alt="MLtraq Logo">\n</p>\n\n<p align="center">\n<img src="https://www.mltraq.com/assets/img/badges/test.svg" alt="Test">\n<img src="https://www.mltraq.com/assets/img/badges/coverage.svg" alt="Coverage">\n<img src="https://www.mltraq.com/assets/img/badges/python.svg" alt="Python">\n<img src="https://www.mltraq.com/assets/img/badges/pypi.svg" alt="PyPi">\n<img src="https://www.mltraq.com/assets/img/badges/license.svg" alt="License">\n<img src="https://www.mltraq.com/assets/img/badges/code-style.svg" alt="Code style">\n</p>\n\n---\n\nOpen source **experiment tracking API** with **ML performance analysis** to build better models faster, facilitating collaboration and transparency within the team and with stakeholders.\n\n---\n\n* **Documentation**: [https://www.mltraq.com](https://www.mltraq.com)\n* **Source code**: [https://github.com/elehcimd/mltraq](https://github.com/elehcimd/mltraq)\n\n---\n\n## Key features\n\n* **Immediate**: start tracking experiments with a few lines of code.\n* **Collaborative**: Backup and upstream experimental results with your team.\n* **Interoperable**: Access the data anywhere with SQL, Pandas and Python API.\n* **Flexible**: Track structured types including Numpy arrays and Pandas frames/series.\n* **Steps library**: Use pre-built "steps" for tracking, testing, analysis and reporting.\n* **Execution engine**: Define and execute parametrized experiment pipelines.\n\n## Requirements\n\n* **Python >=3.10**\n* **SQLAlchemy**, **Pandas**, and **Joblib** (installed as dependencies)\n\n## Installation\n\n```\npip install mltraq\n```\n\n## License\n\nThis project is licensed under the terms of the [BSD 3-Clause License](https://mltraq.com/license).\n\n',
    'author': 'Michele Dallachiesa',
    'author_email': 'michele.dallachiesa@sigforge.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://mltraq.com/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10.0',
}


setup(**setup_kwargs)

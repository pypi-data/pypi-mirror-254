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
    'version': '0.0.107',
    'description': 'Design ML Experiments as State Monads with Persistence',
    'long_description': '<p align="center">\n<img width="33%" height="33%" src="https://mltraq.com/assets/img/logo-wide-black.svg" alt="MLtraq Logo">\n</p>\n\n<p align="center">\n<img src="https://www.mltraq.com/assets/img/badges/test.svg" alt="Test">\n<img src="https://www.mltraq.com/assets/img/badges/coverage.svg" alt="Coverage">\n<img src="https://www.mltraq.com/assets/img/badges/python.svg" alt="Python">\n<img src="https://www.mltraq.com/assets/img/badges/pypi.svg" alt="PyPi">\n<img src="https://www.mltraq.com/assets/img/badges/license.svg" alt="License">\n<img src="https://www.mltraq.com/assets/img/badges/code-style.svg" alt="Code style">\n</p>\n\n---\n\n<h1 align="center">\nDesign ML Experiments as<br>\nState Monads with Persistence\n</h1>\n\nMLtraq is an open-source ML framework for Python that adopts the **state monads** design pattern to model experiments. An `experiment` consists of a collection of `runs` whose state progresses through a chained sequence of `steps`. It incorporates **database persistence** for state recovery and full interoperability using open standards such as Pandas, Arrow and SQL.\n\n---\n\n* **Documentation**: [https://www.mltraq.com](https://www.mltraq.com)\n* **Source code**: [https://github.com/elehcimd/mltraq](https://github.com/elehcimd/mltraq)\n\n---\n',
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

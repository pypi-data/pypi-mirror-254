# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['factorlogged',
 'factorlogged.databases',
 'factorlogged.databases.postgres',
 'factorlogged.middlewares']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=2.0.25,<3.0.0',
 'fastapi>=0.109.0,<0.110.0',
 'paramiko>=3.4.0,<4.0.0',
 'psycopg2>=2.9.9,<3.0.0',
 'sshtunnel>=0.4.0,<0.5.0',
 'uvicorn>=0.27.0,<0.28.0']

setup_kwargs = {
    'name': 'factorlogged',
    'version': '0.1.0',
    'description': 'Middleware logger for FastAPI',
    'long_description': None,
    'author': 'Ricardo Ibarra',
    'author_email': 'raib1997@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

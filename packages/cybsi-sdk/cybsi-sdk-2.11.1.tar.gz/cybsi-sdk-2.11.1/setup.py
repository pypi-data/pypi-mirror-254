# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cybsi',
 'cybsi.api',
 'cybsi.api.artifact',
 'cybsi.api.auth',
 'cybsi.api.data_source',
 'cybsi.api.dictionary',
 'cybsi.api.enrichment',
 'cybsi.api.internal',
 'cybsi.api.license',
 'cybsi.api.observable',
 'cybsi.api.observation',
 'cybsi.api.replist',
 'cybsi.api.report',
 'cybsi.api.search',
 'cybsi.api.user',
 'cybsi.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles==22.1.0',
 'enum-tools==0.9.0.post1',
 'httpx>=0.23.1,<0.24.0',
 'sphinx-jinja2-compat==0.1.1']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.1.1,<5.0.0']}

setup_kwargs = {
    'name': 'cybsi-sdk',
    'version': '2.11.1',
    'description': 'Cybsi development kit',
    'long_description': 'Cybsi SDK\n---------\n\nБиблиотека для взаимодействия с API Threat Analyzer. Позволяет:\n* Настраивать продукт\n* Расширять возможности продукта пользовательскими источниками данных\n* Выгружать и загружать Threat Intelligence в различных форматах\n\nБиблиотека имеет как синхронный, так и асинхронный интерфейс.\n\n[![Supported Versions](https://img.shields.io/pypi/pyversions/cybsi-sdk.svg)](https://pypi.org/project/cybsi-sdk/)\n[![Documentation Status](https://readthedocs.org/projects/cybsi-sdk/badge/?version=latest)](https://cybsi-sdk.readthedocs.io/en/latest/?badge=latest)\n',
    'author': 'Cybsi SDK developers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

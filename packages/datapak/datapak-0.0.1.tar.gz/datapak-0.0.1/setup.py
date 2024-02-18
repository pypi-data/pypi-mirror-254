# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['datapak']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'datapak',
    'version': '0.0.1',
    'description': 'DATAPAK',
    'long_description': '',
    'author': 'Michele Dallachiesa',
    'author_email': 'michele.dallachiesa@sigforge.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10.0',
}


setup(**setup_kwargs)

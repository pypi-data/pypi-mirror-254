# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['csmc', 'csmc.errors', 'csmc.mc']

package_data = \
{'': ['*']}

install_requires = \
['SciPy>=1.11.4,<2.0.0',
 'cvxpy>=1.4.1,<2.0.0',
 'fbpca>=1.0,<2.0',
 'numba>=0.58.1,<0.59.0',
 'threadpoolctl>=3.2.0,<4.0.0',
 'torch>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'csmc',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Antonina Krajewska',
    'author_email': 'antonina.krajewska@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

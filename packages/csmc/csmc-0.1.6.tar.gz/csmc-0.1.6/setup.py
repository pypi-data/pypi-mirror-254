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
    'version': '0.1.6',
    'description': 'Matrix completion with column subset selection.',
    'long_description': '# CSMC \n\nCSMC is a Python library for performing column subset selection in matrix completion tasks. It provides an implementation of the CSSMC method, which aims to complete missing entries in a matrix using a subset of columns.\n\nColumns Selected Matrix Completion (CSMC) is a two-stage approach for low-rank matrix recovery. In the first stage, CSMC samples columns of the input matrix  and recovers a smaller column submatrix.\nIn the second stage, it solves a least squares problem to reconstruct the whole matrix.\n\n<img src="resources/CSMC.png" alt="Alt text" width="400px" />\n\n\n## Installation\n\nYou can install CSMC using pip:\n\n```bash\npip install -i https://test.pypi.org/simple/ csmc\n```\n\n## Usage\n\n```python\nfrom tests.data_generation import create_rank_k_dataset\nfrom csmc import CSMC\n\nn_rows = 300\nn_cols = 1000\nrank = 10\nM, M_incomplete, omega, ok_mask = create_rank_k_dataset(n_rows=n_rows, n_cols=n_cols, k=rank,\n                                                        gaussian=True,\n                                                        fraction_missing=0.8)\nsolver = CSMC(M_incomplete, col_number=400)\nM_filled = solver.fit_transform(M_incomplete)\n```\n\n## Citation\n\nKrajewska, A., Niewiadomska-Szynkiewicz E. (2023). Matrix Completion with Column Subset Selection.',
    'author': 'Antonina Krajewska',
    'author_email': 'antonina.krajewska@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ZAL-NASK/CSMC',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

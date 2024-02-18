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
    'version': '0.1.9',
    'description': 'Matrix completion with column subset selection.',
    'long_description': '# CSMC \n\nCSMC is a Python library for performing column subset selection in matrix completion tasks. It provides an implementation of the CSSMC method, which aims to complete missing entries in a matrix using a subset of columns.\n\nColumns Selected Matrix Completion (CSMC) is a two-stage approach for low-rank matrix recovery. In the first stage, CSMC samples columns of the input matrix  and recovers a smaller column submatrix.\nIn the second stage, it solves a least squares problem to reconstruct the whole matrix.\n\n<img src="resources/CSMC.png" alt="Alt text" width="400px" />\n\n\n## Installation\n\nYou can install CSMC using pip:\n\n```bash\npip install -i  csmc\n```\n\n## Usage\n1. Generate random data\n```python\nimport numpy as np\nimport random \n\nn_rows = 50\nn_cols = 250\nrank = 3\n\nx = np.random.default_rng().normal(size=(n_rows, rank)) \ny = np.random.default_rng().normal(size=(rank, n_cols)) \nM = np.dot(x, y)\n\nM_incomplete = np.copy(M)\nnum_missing_elements = int(0.7 * M.size)\nindices_to_zero = random.sample(range(M.size), k=num_missing_elements)\nrows, cols = np.unravel_index(indices_to_zero, M.shape)\nM_incomplete[rows, cols] = np.nan\n```\n\n2. Fill with CSNN algorithm\n```python\nfrom csmc import CSMC\nsolver = CSMC(M_incomplete, col_number=100)\nM_filled = solver.fit_transform(M_incomplete)\n```\n\n3. Fill with Nuclear Norm Minimization with SDP (NN algorithm)\n\n```python\nfrom csmc import NuclearNormMin\nsolver = NuclearNormMin(M_incomplete)\nM_filled = solver.fit_transform(M_incomplete, np.isnan(M_incomplete))\n```\n\n## Algorithms\n* `NuclearNormMin`: Matrix completion by SDP (NN algorithm) [Exact Matrix Completion via Convex Optimization](http://statweb.stanford.edu/~candes/papers/MatrixCompletion.pdf\n* `CSNN`: Matrix completion by CSNN\n* `PGD`: Nuclear norm minimization using Proximal Gradient Descent (PGD)  [Spectral Regularization Algorithms for Learning Large Incomplete Matrices](http://web.stanford.edu/~hastie/Papers/mazumder10a.pdf) by Mazumder et. al.\n* `CSPGD`: Matrix completion by CSPGD\n\n## Citation\n\nKrajewska, A., Niewiadomska-Szynkiewicz E. (2023). Matrix Completion with Column Subset Selection.\nKrajewska, A. (2023).  [Efficient matrix completion for data recovery in data-driven IT applications](https://www.e-bip.org.pl/upload/00998/37859/1088193-82224218.pdf). Systems Research Institute\nPolish Academy of Sciences.',
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

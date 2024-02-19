# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['benchllama']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['benchllama = benchllama.main:app']}

setup_kwargs = {
    'name': 'benchllama',
    'version': '0.1.0',
    'description': '',
    'long_description': '# `benchllama`\n\nAwesome Portal Gun\n\n**Usage**:\n\n```console\n$ benchllama [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `load`: Load the portal gun\n* `shoot`: Shoot the portal gun\n\n## `benchllama load`\n\nLoad the portal gun\n\n**Usage**:\n\n```console\n$ benchllama load [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `benchllama shoot`\n\nShoot the portal gun\n\n**Usage**:\n\n```console\n$ benchllama shoot [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n',
    'author': 'Srikanth Srungarapu',
    'author_email': 'srikanth235@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

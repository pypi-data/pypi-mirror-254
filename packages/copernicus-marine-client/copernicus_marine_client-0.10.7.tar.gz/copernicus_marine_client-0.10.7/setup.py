# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['copernicus_marine_client',
 'copernicus_marine_client.catalogue_parser',
 'copernicus_marine_client.command_line_interface',
 'copernicus_marine_client.core_functions',
 'copernicus_marine_client.download_functions',
 'copernicus_marine_client.python_interface']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.5,<4.0.0',
 'boto3>=1.25,<1.34',
 'cachier>=2.2.1,<3.0.0',
 'click>=8.0.4,<9.0.0',
 'dask>=2022,<2024',
 'lxml>=4.9.0,<5.0.0',
 'motuclient>=1.8.4,<2.0.0',
 'nest-asyncio>=1.5.8,<2.0.0',
 'netCDF4>=1.6.3,<2.0.0',
 'pydap>=3.2.2,<4.0.0',
 'pystac>=1.8.3,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'semver>=3.0.2,<4.0.0',
 'setuptools>=68.2.2,<69.0.0',
 'tqdm>=4.65.0,<5.0.0',
 'xarray>=2023.9,<2023.12',
 'zarr>=2.13.3,<3.0.0']

entry_points = \
{'console_scripts': ['copernicus-marine = '
                     'copernicus_marine_client.command_line_interface.copernicus_marine:command_line_interface']}

setup_kwargs = {
    'name': 'copernicus-marine-client',
    'version': '0.10.7',
    'description': '',
    'long_description': '⚠️⚠️⚠️ The `coernicus-marine-client` PyPI package is deprecated. Please use `copernicusmarine` instead ⚠️⚠️⚠️\n\nHere is the link to the new pypi repository: [https://pypi.org/project/copernicusmarine/](https://pypi.org/project/copernicusmarine/)"\nOr install it using the following command: `pip install copernicusmarine`\n\nIf you were using this deprecated version, you may also want to delete the following folders:\n\n- `~/.copernicus-marine-client`\n- `~/.cachier` (⚠️ Be carefull with this one as it can contains other stuffs unrelated to the `copernicus-marine-client` package !)\n\n# Reason for the deprecation\n\nThe official version 1.0.0 of the package has been released and it has been decided to rename the package to `copernicusmarine`.\nThat way, the command will always be the same, no matter what interface you are using (python or CLI).\n',
    'author': 'Copernicus Marine User Support',
    'author_email': 'servicedesk.cmems@mercator-ocean.eu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)

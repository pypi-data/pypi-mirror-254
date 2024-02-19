# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['ahn_cli', 'ahn_cli.fetcher', 'ahn_cli.manipulator']

package_data = \
{'': ['*'],
 'ahn_cli.fetcher': ['data/ahn_grid.geojson',
                     'data/ahn_grid.geojson',
                     'data/ahn_grid.geojson',
                     'data/ahn_grid.geojson',
                     'data/ahn_subunit.geojson',
                     'data/ahn_subunit.geojson',
                     'data/ahn_subunit.geojson',
                     'data/ahn_subunit.geojson',
                     'data/municipality.geojson',
                     'data/municipality.geojson',
                     'data/municipality.geojson',
                     'data/municipality.geojson',
                     'data/municipality_simple.geojson',
                     'data/municipality_simple.geojson',
                     'data/municipality_simple.geojson',
                     'data/municipality_simple.geojson']}

install_requires = \
['click>=8.1.7,<9.0.0',
 'geopandas>=0.14.1,<0.15.0',
 'laspy[lazrs]>=2.5.3,<3.0.0',
 'pdal>=3.2.3,<4.0.0',
 'pyvista>=0.43.1,<0.44.0',
 'requests>=2.31.0,<3.0.0',
 'shapely>=2.0.2,<3.0.0']

entry_points = \
{'console_scripts': ['ahn_cli = ahn_cli.main:main']}

setup_kwargs = {
    'name': 'ahn-cli',
    'version': '0.1.5',
    'description': '',
    'long_description': "# AHN CLI\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n[![Version: 1.0.0](https://img.shields.io/badge/Version-0.1.0-green.svg)](https://github.com/HideBa/ahn-cli/releases/tag/v0.1.0)\n[![CICD Status: Passing](https://img.shields.io/badge/CICD-Passing-brightgreen.svg)](https://github.com/HideBa/ahn-cli/actions)\n\n## Description\n\nAHN CLI is a command-line interface tool designed for the effortless downloading of AHN (Actueel Hoogtebestand Nederland) point cloud data for specific cities and classification classes.\n\n## Installation\n\n> **NOTE:** AHN CLI requires PDAL to be installed on your system. Follow the installation instructions in the [PDAL documentation](https://pdal.io/download.html) before proceeding.\n\nInstall AHN CLI using pip:\n\n```\npip install ahn_cli\n```\n\n## Usage\n\nTo utilize the AHN CLI, execute the following command with the appropriate options:\n\n```shell\nOptions:\n -c, --city <city_name>        Download point cloud data for the specified city.\n -o, --output <file>           Designate the output file for the downloaded data.\n -i, --include-class <class>   Include specific point cloud classes in the download,\n                               specified in a comma-separated list. Available classes:\n                               0:Created, never classified; 1:Unclassified; 2:Ground;\n                               6:Building; 9:Water; 14:High tension; 26:Civil structure.\n -e, --exclude-class <class>   Exclude specific point cloud classes from the download,\n                               specified in a comma-separated list. Available classes as above.\n -d, --decimate <step>         Decimate the point cloud data by the specified step.\n -ncc, --no-clip-city          Avoid clipping the point cloud data to the city boundary.\n -cf, --clip-file <file>       Provide a file path for a clipping boundary file to clip\n                               the point cloud data to a specified area.\n -r, --radius <radius>         Define a radius (in meters) to clip the point cloud data,\n                               centered on the city polygon.\n -p, --preview                 Preview the point cloud data in a 3D viewer.\n -h, --help [category]         Show help information. Optionally specify a category for\n                               detailed help on a specific command.\n -v, --version                 Display the version number of the AHN CLI and exit.\n```\n\n### Usage Examples\n\n**Download Point Cloud Data for Delft with All Classification Classes:**\n\n```\nahn_cli -c delft -o ./delft.laz\n```\n\n**To Include or Exclude Specific Classes:**\n\n```\nahn_cli -c delft -o ./delft.laz -i 1,2\n```\n\n**For Non-Clipped, Rectangular-Shaped Data:**\n\n```\nahn_cli -c delft -o ./delft.laz -i 1,2 -ncc\n```\n\n**To Decimate City-Scale Point Cloud Data:**\n\n```\nahn_cli -c delft -o ./delft.laz -i 1,2 -d 2\n```\n\n**Specify a Radius for Clipping:**\n\nIf you specify a `radius` (in meters), it will clip the point cloud data from the center of the city polygon to the specified radius.\n\n## Reporting Issues\n\nEncountering issues or bugs? We greatly appreciate your feedback. Please report any problems by opening an issue on our GitHub repository. Be as detailed as possible in your report, including steps to reproduce the issue, the expected outcome, and the actual result. This information will help us address and resolve the issue more efficiently.\n\n## Contributing\n\nYour contributions are welcome! If you're looking to contribute to the AHN CLI project, please first review our Contribution Guidelines. Whether it's fixing bugs, adding new features, or improving documentation, we value your help.\n\nTo get started:\n\n- Fork the repository on GitHub.\n- Clone your forked repository to your local machine.\n- Create a new branch for your contribution.\n- Make your changes and commit them with clear, descriptive messages.\n  Push your changes to your fork.\n- Submit a pull request to our repository, providing details about your changes and the value they add to the project.\n- We look forward to reviewing your contributions and potentially merging them into the project!\n",
    'author': 'HideBa',
    'author_email': 'baba.papa1120.ba@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)

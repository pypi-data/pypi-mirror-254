# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['majormode',
 'majormode.xebus',
 'majormode.xebus.constant',
 'majormode.xebus.model',
 'majormode.xebus.utils']

package_data = \
{'': ['*']}

install_requires = \
['mercurius-core-library>=1.0,<2.0', 'perseus-core-library>=1.19,<2.0']

setup_kwargs = {
    'name': 'xebus-core-library',
    'version': '1.4.7',
    'description': 'Xebus Core Python Library',
    'long_description': '# Xebus Core Python Library\n\nXebus Core Python Library is a repository of reusable Python components to be shared by Python projects using the Xebus RESTful API.\n\nThese components have minimal dependencies on other libraries, so that they can be deployed easily.  In addition, these components will keep their interfaces as stable as possible, so that other Python projects can integrate these components without having to worry about changes in the future.\n',
    'author': 'Daniel CAUNE',
    'author_email': 'daniel.caune@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xebus/xebus-core-python-library',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['no_action']

package_data = \
{'': ['*'], 'no_action': ['templates/*']}

install_requires = \
['jinja2>=3.1.3,<4.0.0', 'loguru>=0.7.2,<0.8.0']

setup_kwargs = {
    'name': 'no-action',
    'version': '0.7.0',
    'description': 'no_action is an incremental automation library to eliminate toil in processes.',
    'long_description': "# no_action\n\nAn incremental automation library to eliminate toil in processes.\n\n## Description\n\nIdeologically based on Dan Slimmon's [Do-nothing scripting][dns] article from 2019. `no_action`\nprovides a `Step` class that can be sub-classed and customized as well as a `Prodecure` class that\nwraps a series of ordered steps.\n\nFirst, one writes a series of Steps with the manual details in their docstring and the procedure\nprints the docstrings, a glorified checklist. Over time though, with each Step encapsulated in\na discrete class, Steps of a procedure can be automated by writing code that actually does what is\ndescribed in the docstring (override the `Step.execute()` method). Soon, your procedures are fully\nautomated and can be hooked into an Internal Developer Platform (IDP), a runner, or other automation\norchestration system.\n\n[dns]: https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/#\n\n## Installation\n\nThis library can be found on PyPI. Run the following command to install the library into your\nproject.\n\n`python3 -m pip install no-action`\n\n<!--\n## Usage\n\nUse examples liberally, and show the expected output if you can. It's helpful to have inline the\nsmallest example of usage that you can demonstrate, while providing links to more sophisticated\nexamples if they are too long to reasonably include in the README.\n\n## Support\n\nTell people where they can go to for help. It can be any combination of an issue tracker, a chat\nroom, an email address, etc.\n\n## Contributing\n\nState if you are open to contributions and what your requirements are for accepting them.\n\nFor people who want to make changes to your project, it's helpful to have some documentation on how\nto get started. Perhaps there is a script that they should run or some environment variables that\nthey need to set. Make these steps explicit. These instructions could also be useful to your future\nself.\n\nYou can also document commands to lint the code or run tests. These steps help to ensure high code\nquality and reduce the likelihood that the changes inadvertently break something. Having\ninstructions for running tests is especially helpful if it requires external setup, such as starting\na Selenium server for testing in a browser.\n\n## Authors and acknowledgment\n\nShow your appreciation to those who have contributed to the project.\n-->\n\n## License\n\nThis project is licensed under the GNU GPL 3. See;\n\n- [LICENSE](.LICENSE) for the preamble.\n- [COPYING](./COPYING) for the full text.\n",
    'author': 'Nicholas Skoretz',
    'author_email': 'nskoretz@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)

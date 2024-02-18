# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['playwright_trace_browser']

package_data = \
{'': ['*']}

install_requires = \
['more-itertools>=10.2.0,<11.0.0',
 'playwright>=1.41.1,<2.0.0',
 'textual>=0.48.1,<0.49.0']

setup_kwargs = {
    'name': 'playwright-trace-browser',
    'version': '1.0.0',
    'description': 'A TUI app for exploring Playwright traces',
    'long_description': '\n\n[![](https://codecov.io/gh/nickderobertis/playwright-trace-browser/branch/main/graph/badge.svg)](https://codecov.io/gh/nickderobertis/playwright-trace-browser)\n[![PyPI](https://img.shields.io/pypi/v/playwright-trace-browser)](https://pypi.org/project/playwright-trace-browser/)\n![PyPI - License](https://img.shields.io/pypi/l/playwright-trace-browser)\n[![Documentation](https://img.shields.io/badge/documentation-pass-green)](https://nickderobertis.github.io/playwright-trace-browser/)\n![Tests Run on Ubuntu Python Versions](https://img.shields.io/badge/Tests%20Ubuntu%2FPython-3.9%20%7C%203.10-blue)\n![Tests Run on Macos Python Versions](https://img.shields.io/badge/Tests%20Macos%2FPython-3.9%20%7C%203.10-blue)\n![Tests Run on Windows Python Versions](https://img.shields.io/badge/Tests%20Windows%2FPython-3.9%20%7C%203.10-blue)\n[![Github Repo](https://img.shields.io/badge/repo-github-informational)](https://github.com/nickderobertis/playwright-trace-browser/)\n\n\n#  playwright-trace-browser\n\n## Overview\n\nA TUI app for exploring Playwright traces\n\n## Getting Started\n\nInstall `playwright-trace-browser`:\n\n```\npip install playwright-trace-browser\n```\n\nA simple example:\n\n```python\nimport playwright_trace_browser\n\n# Do something with playwright_trace_browser\n```\n\nSee a\n[more in-depth tutorial here.](\nhttps://nickderobertis.github.io/playwright-trace-browser/tutorial.html\n)\n\n## Links\n\nSee the\n[documentation here.](\nhttps://nickderobertis.github.io/playwright-trace-browser/\n)\n\n## Development Status\n\nThis project is currently in early-stage development. There may be\nbreaking changes often. While the major version is 0, minor version\nupgrades will often have breaking changes.\n\n## Developing\n\nSee the [development guide](\nhttps://github.com/nickderobertis/playwright-trace-browser/blob/main/DEVELOPING.md\n) for development details.\n\n## Author\n\nCreated by Nick DeRobertis. MIT License.\n\n',
    'author': 'Nick DeRobertis',
    'author_email': 'derobertis.nick@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

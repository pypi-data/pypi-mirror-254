# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lmoe', 'lmoe.experts']

package_data = \
{'': ['*']}

install_requires = \
['ollama>=0.1.6,<0.2.0', 'pyperclip>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['lmoe = lmoe.main:run']}

setup_kwargs = {
    'name': 'lmoe',
    'version': '0.1.0',
    'description': "LMoE (Local mixture of experts, pronounced 'Elmo') is your CLI assistant for general knowledge, coding, and image analysis.",
    'long_description': '# lmoe\n\nlmoe (pronounced "Elmo") is a multimodal CLI assistant which interacts with natural language. It is a local Mixture of Experts (MoE), hence the name LMoE (or lmoe).\n\nRunning on Ollama and various open-weight models, lmoe is intended to be a convenient, low overhead, low configuration way to interact with AI models from the command line.\n\n## Status\n\nVersion 0.1.0\n\nThis is currently a very basic implementation which only supports a general expert, no configuration, does not automate environment setup, and does not have persistence.\n\nIn the words of many a developer, "it runs fine on my machine" but is currently not intended for general use.\n\n### Upcoming features\n\n* pip integration\n* self-setup (after installing with pip)\n* configurability\n* integration with code and image models\n* persisted context (i.e. memory, chat-like experience without a formal chat interface)\n',
    'author': 'Ryan Eiger',
    'author_email': 'ryebosome@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

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
    'version': '0.1.1',
    'description': "LMoE (Local mixture of experts, pronounced 'Elmo') is your CLI assistant for general knowledge, coding, and image analysis.",
    'long_description': '# lmoe\n\nlmoe (pronounced "Elmo", a local Mixture of Experts) is a multimodal CLI assistant with a natural\nlanguage interface.\n\nRunning on Ollama and various open-weight models, lmoe is intended to be a convenient, low-overhead,\nlow-configuration way to interact with AI models from the command line.\n\n## Examples\n\nlmoe has a natural language interface and no syntactic overhead or commands to remember.\n\nYou will need to quote your strings if you want to use characters that are significant to your shell\n(like `?`).\n\n### Querying\n```\n% lmoe who was matisse\n\n Henri Matisse was a French painter, sculptor, and printmaker, known for his influential role in\n modern art. He was born on December 31, 1869, in Le Cateau-Cambrésis, France, and died on\n November 3, 1954. Matisse is recognized for his use of color and his fluid and expressive\n brushstrokes. His works include iconic paintings such as "The Joy of Life" and "Woman with a Hat."\n```\n\n```\n% lmoe what is the recommended layout for a python project with poetry\n\n With Poetry, a Python packaging and project management tool, a recommended layout for a Python\n project could include the following structure:\n\n myproject/\n ├── pyproject.toml\n ├── README.rst\n ├── requirements.in\n └── src/\n     ├── __init__.py\n     └── mypackage/\n         ├── __init__.py\n         ├── module1.py\n         └── module2.py\n\nIn this layout, the `myproject/` directory contains the root-level project files. The\n`pyproject.toml` file is used for managing dependencies and building your Python package. The\n`README.rst` file is optional, but common, to include documentation about your project. The\n`requirements.in` file lists the external packages required by your project.\n\nThe `src/` directory contains your source code for the project. In this example, there\'s a package\nnamed `mypackage`, which includes an `__init__.py` file and two modules: `module1.py` and\n`module2.py`.\n\nThis is just one suggested layout using Poetry. Depending on your specific project requirements and\npreferences, the layout might vary. Always refer to the [Poetry documentation](https://python-poetry.org/)\nfor more detailed information.\n```\n\n### Querying your context\n\n#### Piping context\n\nPipe it information from your computer and ask questions about it.\n\n```\n% cat projects/lmoe/lmoe/main.py | lmoe what does this code do\n\n The provided code defines a Python script named \'lmoe\' which includes an argument parser, the\n ability to read context from both STDIN and the clipboard, and a \'classifier\' module for\n determining which expert should respond to a query without actually responding. It does not contain\n any functionality for executing queries or providing responses itself. Instead, it sets up the\n infrastructure for interfacing with external experts through their \'generate\' methods.\n```\n\n```\n% print -x \'hello\'\n\nprint: positive integer expected after -x: hello\n\n% echo \'print: positive integer expected after -x: hello\' | lmoe \'why am I getting this error with the `print` shell command?\'\n\n The `print` command in a Unix-like shell expects a positive integer as its argument to print that\n value to the console. You provided the string \'hello\' instead, which is causing the error message\n you\'re seeing.\n```\n\n```\n% ls -la | lmoe how big is my zsh history\n\n The size of your Zsh history file is 16084 bytes.\n```\n\n#### Pasting context\n\nLet\'s copy the following code to the clipboard.\n\n```shell\n# Define the base directory for virtual environments\nVENVS_DIR="$HOME/.venvs"\n\n# Helper for manipulating Python virtual environments\nvenv() {\n    if [[ $# -lt 1 ]]; then\n        echo "Usage: venv <command> [args]"\n        exit 1\n    fi\n\n    command="$1"\n    shift\n\n    case "$command" in\n        mkdir)\n            if [[ $# -lt 1 ]]; then\n                echo "Usage: venv mkdir <env_name>"\n                exit 1\n            fi\n            python3 -m venv "$VENVS_DIR/$1"\n            ;;\n        ls)\n            ls "$VENVS_DIR"\n            ;;\n        rm)\n            if [[ $# -lt 1 ]]; then\n                echo "Usage: venv rm <env_name>"\n                exit 1\n            fi\n            echo "Do you want to remove $1? (y/n): \\c"\n            read confirm\n            if [[ $confirm == "y" ]]; then\n                rm -rf "$VENVS_DIR/$1"\n            fi\n            ;;\n        activate)\n            if [ -z "$1" ]; then\n            . "$VENVS_DIR/default/bin/activate"\n            else\n            . "$VENVS_DIR/$1/bin/activate"\n            fi\n            ;;\n        *)\n            echo "Unknown command. Available commands: mkdir, ls, rm, activate"\n            exit 1\n            ;;\n    esac\n}\n```\n\n```\n% lmoe --paste what does this zsh script do\n\n This zsh script defines a function named `venv` that assists in managing Python virtual\n environments. It provides several subcommands: "mkdir" for creating new environments, "ls" for\n listing existing environments, "rm" for removing environments, and "activate" for activating an\n environment. The base directory for all virtual environments is set to `$HOME/.venvs`.\n```\n\n### Code Generation\n\nComing soon.\n\n### Images\n\nComing soon.\n\n## Status\n\nVersion 0.1.01\n\nThis is currently a very basic implementation which only supports a general expert, no\nconfiguration, does not automate environment setup, and does not have persistence.\n\nIn the words of many a developer, "it runs fine on my machine" but is currently not intended for\nothers\' use.\n\n### Upcoming features\n\n* integration with code and image models\n* self-setup (after installing with pip)\n* persisted context (i.e. memory, chat-like experience without a formal chat interface)\n* configurability\n',
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

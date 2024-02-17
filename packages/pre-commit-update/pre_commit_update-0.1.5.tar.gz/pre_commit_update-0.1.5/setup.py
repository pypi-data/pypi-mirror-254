# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pre_commit_update']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1,<4.0',
 'click>=8.1,<9.0',
 'packaging>=23.2,<24.0',
 'pyproject-parser>=0.9,<0.10',
 'ruamel.yaml>=0.18,<0.19']

entry_points = \
{'console_scripts': ['pre-commit-update = pre_commit_update.cli:cli']}

setup_kwargs = {
    'name': 'pre-commit-update',
    'version': '0.1.5',
    'description': 'Simple CLI tool to check and update pre-commit hooks.',
    'long_description': '# pre-commit-update\n\n![Version](https://img.shields.io/pypi/pyversions/pre-commit-update)\n![Downloads](https://pepy.tech/badge/pre-commit-update)\n![Formatter](https://img.shields.io/badge/code%20style-black-black)\n![License](https://img.shields.io/pypi/l/pre-commit-update)\n\n**pre-commit-update** is a simple CLI tool to check and update pre-commit hooks.\n\n## Table of contents\n\n1. [ Reasoning ](#reasoning)\n2. [ Features ](#features)\n3. [ Installation ](#installation)\n4. [ Usage ](#usage)\n    1. [ Pipeline usage example ](#pipeline-usage-example)\n    2. [ pre-commit hook usage example ](#pre-commit-hook-usage-example)\n    3. [ pyproject.toml usage example ](#pyprojecttoml-usage-example)\n\n## Reasoning\n\n`pre-commit` is a nice little tool that helps you polish your code before releasing it into the wild.\nIt is fairly easy to use. A single `pre-commit-config.yaml` file can hold multiple hooks (checks) that will go through\nyour code or repository and do certain checks. The problem is that the file is static and once you pin your hook versions\nafter a while they get outdated.\n\n`pre-commit-update` was created because there is no easy way to update your hooks by using\n`pre-commit autoupdate` as it is not versatile enough.\n\n\n## Features\n\n|                      Feature                       | pre-commit-update |            pre-commit autoupdate            |\n|:--------------------------------------------------:|:-----------------:|:-------------------------------------------:|\n|   Dry run (checks for updates, does not update)    |        Yes        |                     No                      |\n|                Stable versions only                |        Yes        |                     No                      |\n|         Exclude repo(s) from update check          |        Yes        | Workaround (updates only specified repo(s)) |\n| Keep repo(s) (checks for updates, does not update) |        Yes        |                     No                      |\n|           Update by hash instead of tag            |        Yes        |                     Yes                     |\n|          Can be used as a pre-commit hook          |        Yes        |                     No                      |\n|       Can be configured in `pyproject.toml`        |        Yes        |                     No                      |\n\n\n## Installation\n\n`pre-commit-update` is available on PyPI:\n```console \n$ python -m pip install pre-commit-update\n```\nPython >= 3.7 is supported.\n\n**NOTE:** Please make sure that `git` is installed.\n\n\n## Usage\n\n`pre-commit-update` CLI can be used as below:\n\n```console\nUsage: pre-commit-update [OPTIONS]\n\nOptions:\n  -d, --dry-run       Dry run only checks for the new versions without\n                      updating\n  -a, --all-versions  Include the alpha/beta versions when updating\n  -v, --verbose       Display the complete output\n  -e, --exclude TEXT  Exclude specific repo(s) by the `repo` url trim\n  -k, --keep TEXT     Keep the version of specific repo(s) by the `repo` url trim (still checks for the new versions)\n  -h, --help          Show this message and exit.\n```\n\nIf you want to just check for updates (without updating `pre-commit-config.yaml`), for example, you would use:\n```console\n$ pre-commit-update -d\n```\nor\n```console\n$ pre-commit-update --dry-run\n```\n\n**NOTE:** If you are to use the `exclude` or `keep` options, please pass the repo url trim as a parameter.\nKeep in mind that if you have multiple hooks (id\'s) configured for a single repo and you `exclude` that repo,\n**NONE** of the hooks will be updated, whole repo will be excluded.\n\nExample of repo url trim: https://github.com/ambv/black -> `black` (you will only pass `black` as a parameter to\n`exclude` or `keep`)\n\n### Pipeline usage example\n#### GitLab job:\n\n```yaml\npre-commit-hooks-update:\n  stage: update\n  script:\n    # install git if not present in the image\n    - pip install pre-commit-update\n    - pre-commit-update --dry-run\n  except:\n    - main\n  when: manual\n  allow_failure: true\n```\n\n**NOTE:** This is just an example, feel free to do your own configuration\n\n### pre-commit hook usage example\n\nYou can also use `pre-commit-update` as a hook in your `pre-commit` hooks:\n\n```yaml\n- repo: https://gitlab.com/vojko.pribudic/pre-commit-update\n  rev: v0.1.2  # Insert the latest tag here\n  hooks:\n    - id: pre-commit-update\n      args: [--dry-run --exclude black --keep isort]\n```\n\n### pyproject.toml usage example\n\nYou can configure `pre-commit-update` in your `pyproject.toml` as below (feel free to do your own configuration):\n\n```toml\n[tool.pre-commit-update]\ndry_run = true\nall_versions = false\nverbose = true\nexclude = ["isort"]\nkeep = ["black"]\n```\n\n**NOTE:** If some of the options are missing (for example `exclude` option), `pre-commit-update`\nwill use default value for that option (default for `exclude` option would be an empty list).\n\n***IMPORTANT*** If you invoke `pre-commit-update` with any flags (e.g. `pre-commit-update -d`),\n`pyproject.toml` configuration will be **ignored**. If you configure `pre-commit-update` via `pyproject.toml`\nyou should only run `pre-commit-update` (without any flags / arguments).\n',
    'author': 'Vojko Pribudić',
    'author_email': 'dmanthing@gmail.com',
    'maintainer': 'Vojko Pribudić',
    'maintainer_email': 'dmanthing@gmail.com',
    'url': 'https://gitlab.com/vojko.pribudic/pre-commit-update',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)

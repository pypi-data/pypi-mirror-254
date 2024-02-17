# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['memfault_cli']

package_data = \
{'': ['*']}

install_requires = \
['Click>=7,<9',
 'chardet<5.0',
 'mflt-build-id>=1.0.1,<2.0.0',
 'mflt-pyelftools>=0.30.1,<0.31.0',
 'more-itertools>=8.0.2',
 'pyaxmlparser>=0.3.24,<0.4.0',
 'pyserial>=3.5,<4.0',
 'requests>=2.27.1,<3.0.0',
 'tqdm>=4.44.1,<5.0.0',
 'urllib3>=1.26.7']

extras_require = \
{':python_version < "3.7"': ['dataclasses==0.8'],
 ':python_version < "3.8"': ['importlib-metadata==4.8.3']}

entry_points = \
{'console_scripts': ['memfault = memfault_cli.cli:main']}

setup_kwargs = {
    'name': 'memfault-cli',
    'version': '1.0.7',
    'description': 'Memfault CLI tool',
    'long_description': "# Memfault CLI tool\n\nThis package contains the `memfault` CLI tool.\n\nThe purpose of the tool is to make integration with Memfault from other systems,\nlike continuous integration servers, as easy as possible.\n\nInstall the tool and run `memfault --help` for more info!\n\n## Changes\n\n### 1.0.7\n\n- Fix bug when deactivating delta releases when multiple deployments match  \n  the filters.\n\n### 1.0.6\n\n- Source pyelftools from https://github.com/memfault/pyelftools while we are\n  waiting for 2 bugfixes to get merged upstream\n  (https://github.com/eliben/pyelftools/pull/537 and\n  https://github.com/eliben/pyelftools/pull/538).\n\n### 1.0.5\n\n- Add support for deactivating delta releases.\n\n### 1.0.4\n\n- Add `upload-elf-symbols` command for uploading ELF files with debug symbols\n  built outside of a Yocto environment\n- Add `upload-elf-coredump` for uploading a Linux coredump to Memfault\n\n### 1.0.3\n\n- Fix a bug where `upload-aosp-symbols` would fail when uploading too many files\n  at once.\n\n### 1.0.2\n\n- Fix a bug where `upload-yocto-symbols` would fail when some files in the\n  tarballs provided did not have the read permission set.\n\n### 1.0.1\n\n- Fix `upload-custom-data-recording` to print a more helpful error message when\n  exceeding device rate limits.\n\n### 1.0.0\n\n_Note: this release is marked as `1.0.0` but does not contain any breaking\nchanges! The version number was bumped to reflect the maturity of the tool._\n\n- Fix `upload-mcu-symbols` to skip uploading if the symbol file has already been\n  uploaded, and return a zero exit code in this case\n\n### 0.18.1\n\n- Add the `--deactivate` option to `deploy-release`, which disables a release\n  for a cohort\n\n### 0.18.0\n\n- Add new `extra-metadata` option to `upload-ota-payload` to attach custom\n  metadata to that OTA release. The metadata will be returned from Memfault\n  Cloud when fetching the latest Android OTA release.\n- Continue uploading the entire folder of symbols even if any single upload\n  fails due to the symbol file being too large.\n\n### 0.17.0\n\n- Add new `console` command to read SDK exported chunks via a serial port and\n  automatically upload to Memfault.\n\n### 0.16.0\n\n- Add support for uploading Android debug symbols from alternative build\n  systems.\n\n### 0.15.3\n\n- Warn if a non-slug string is passed to the `--project` or `--org` arguments\n\n### 0.15.2\n\n- Don't truncate help output from `click` when the `CI` environment variable is\n  set, for consistent output formatting\n\n### 0.15.1\n\n- Fix some compatibility issues for python3.6 + python3.7\n\n### 0.15.0\n\n- 💥 Breaking change: update the `upload-yocto-symbols` subcommand to take two\n  image paths as required arguments; one for the root filesystem image, and\n  another for the debug filesystem image. Versions 0.14.0 and lower used to take\n  a guess at the path of the debug filesystem image from the value passed to the\n  `--image` param. To avoid confusion and to support all configurations, the\n  Memfault CLI no longer does any guessing and now takes two separate params:\n  `--image` and `--dbg-image`\n\n### 0.14.0\n\n- ✨ Update the `post-chunk` subcommand to split uploads into batches of 500\n  chunks per upload, to avoid timing out when uploading very large chunk logs\n\n### 0.13.0\n\n- 💥 Breaking change: Renamed subcommand `upload-debug-data-recording` to\n  `custom-data-recording`\n\n### 0.12.0\n\n- ✨ Added subcommand `upload-debug-data-recording` for uploading debug data\n  files\n\n### 0.11.0\n\n- ✨ Enable support for Yocto Dunfell based projects (previously supported\n  Kirkstone only)\n\n### 0.10.0\n\n- ✨ Upload-yocto-symbols now uploads additional symbol files\n\n### 0.9.0\n\n- ✨ Expanded support for .elf uploading with the upload-yocto-symbols\n  subcommand\n\n### 0.8.0\n\n- ✨ Initial support for upload-yocto-symbols subcommand\n\n### 0.7.0\n\n- 🐛 Updated to correctly only use the GNU build-id `.note` section\n",
    'author': 'Memfault Inc',
    'author_email': 'hello@memfault.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://docs.memfault.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

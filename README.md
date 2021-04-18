![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/aiopymake/aiorequest.svg?branch=master)](https://travis-ci.org/aiopymake/aiorequest)
[![Coverage Status](https://coveralls.io/repos/github/aiopymake/aiorequest/badge.svg?branch=master)](https://coveralls.io/github/aiopymake/aiorequest?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with interrogate](https://img.shields.io/badge/interrogate-checked-yellowgreen)](https://interrogate.readthedocs.io/en/latest/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![CodeFactor](https://www.codefactor.io/repository/github/aiopymake/aiorequest/badge)](https://www.codefactor.io/repository/github/aiopymake/aiorequest)
[![PyPI version shields.io](https://img.shields.io/pypi/v/aiorequest.svg)](https://pypi.python.org/pypi/aiorequest/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/aiorequest.svg)](https://pypi.python.org/pypi/aiorequest/)
[![PyPi downloads](https://img.shields.io/pypi/dm/aiorequest.svg)](https://pypi.python.org/pypi/aiorequest)
[![Downloads](https://pepy.tech/badge/aiorequest)](https://pepy.tech/project/aiorequest)

# aioRequest

> Provides asynchronous user-friendly micro HTTP client with nothing but clean objects.

> Basically, it is a wrapper over **requests** python library with async/await approach.
> Represents asynchronous version of [urequest](https://upymake.github.io/urequest/) package.

## Tools

### Production

- python 3.7, 3.8
- [asyncio](https://docs.python.org/3/library/asyncio.html) library
- [requests](https://requests.readthedocs.io/en/master) library

### Development

- [travis](https://travis-ci.org/) CI
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)
- [interrogate](https://interrogate.readthedocs.io/en/latest)
- [bats](https://github.com/bats-core/bats-core)

## Usage

### Installation

```bash
pip install aiorequest
✨ 🍰 ✨
```

### Quick start

```python
>>> import asyncio
>>> from typing import Tuple
>>> from aiorequest.sessions import Session, HttpSession
>>> from aiorequest.responses import HTTPStatus, Response, JsonType
>>> from aiorequest.urls import HttpUrl
>>>
>>>
>>> async def aioresponse() -> Tuple[HTTPStatus, JsonType]:
...     session: Session
...     async with HttpSession() as session:
...         response: Response = await session.get(
...             HttpUrl(host="xkcd.com", path="info.0.json")
...         )
...         return await response.status(), await response.as_json()
... 
... 
>>>
>>> asyncio.run(aioresponse())
(
  <HTTPStatus.OK: 200>,
  {
    "month": "3",
    "num": 2284,
    "link": "",
    "year": "2020",
    "news": "",
    "safe_title": "Sabotage",
    "transcript": "",
    "img": "https://imgs.xkcd.com/comics/sabotage.png",
    "title": "Sabotage",
    "day": "23",
  }
)
```

### Source code

```bash
git clone git@github.com:aiopymake/aiorequest.git
python setup.py install
```

Or using specific release:
```bash
pip install git+https://github.com/aiopymake/aiorequest@0.0.1
```

### Local debug

```bash
git clone git@github.com:aiopymake/aiorequest.git
```

```python
>>> import aiorequest
>>> aiorequest.__doc__
'Package provides asynchronous user-friendly HTTP client with clean objects.'
```

**[⬆ back to top](#aiorequest)**

## Development notes

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle` and `interrogate`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

The package is also covered with the installation unit tests based on [bats](https://github.com/bats-core/bats-core) framework. Please run the following command to launch package unit tests:
```bash
bats --pretty test-package.bats
```

> `PACKAGE_NAME` and `PACKAGE_VERSION` environment variables should be specified prelimirary.

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [AUTHORS](AUTHORS.md) file for all contributors.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/aiopymake/aiorequest/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#aiorequest)**

# pytest-lock

## Overview
[![License MIT](https://img.shields.io/badge/license-MIT-blue)](https://codecov.io/gh/athroniaeth/pytest-lock)
[![Python versions](https://img.shields.io/pypi/pyversions/bandit.svg)](https://pypi.python.org/pypi/bandit)
[![PyPI version](https://badge.fury.io/py/pytest-lock.svg)](https://pypi.org/project/pytest-lock/)
[![codecov](https://codecov.io/gh/Athroniaeth/pytest-lock/graph/badge.svg?token=28E1OZ144W)](https://codecov.io/gh/Athroniaeth/pytest-lock)
[![Workflow](https://img.shields.io/github/actions/workflow/status/Athroniaeth/pytest-lock/release.yml)]("https://github.com/Athroniaeth/pytest-lock/actions/workflows/release.yml")
[![Documentation Status](https://readthedocs.org/projects/pytest-lock/badge/?version=latest)](https://pytest-lock.readthedocs.io/en/latest/)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

**pytest-lock** is a pytest plugin that allows you to "lock" the results of unit tests, storing them in a local cache.
This is particularly useful for tests that are resource-intensive or don't need to be run every time. When the tests are
run subsequently. **pytest-lock** will compare the current results with the locked results and issue a warning if there
are any discrepancies.

* Free software: Apache license
* Documentation: https://pytest-lock.readthedocs.io/en/latest/
* Source: https://github.com/Athroniaeth/pytest-lock
* Bugs: https://github.com/Athroniaeth/pytest-lock/issues
* Contributing: https://github.com/Athroniaeth/pytest-lock/blob/main/CONTRIBUTING.md


## Installation

To install pytest-lock, you can use pip:

```bash
pip install pytest-lock
```

## Usage

### Locking Tests

To lock a test, use the lock fixture. Here's an example:

```python
from pytest_lock import FixtureLock


def test_lock_sum(lock: FixtureLock):
    args = [1, 2, 3]
    lock.lock(sum, (args,))
    ...
```

Run pytest with the `--lock` option to generate the lock files:

```bash
pytest --lock
```

This will generate JSON files in a `.pytest-lock` directory, storing the results of the locked tests.

### Running Tests

Simply run pytest as you normally would:

```bash
pytest
```

If pytest detect the presence of lock fixtures in your tests, it will compare the results of the tests with the locked
If a test result differs from its locked value, a warning will be issued.

### Configuration

The locked test results are stored in a `.pytest-lock` directory at the root of your project. You can delete this
directory to reset all locks.

## Contributing

Contributions are welcome! Please read the contributing guidelines to get started.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

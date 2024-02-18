# numerous SDK

![pipeline](https://gitlab.com/numerous/numerous.sdk/badges/main/pipeline.svg)
![coverage](https://gitlab.com/numerous/numerous.sdk/badges/main/coverage.svg?job=pytest)
![Documentation Status](https://readthedocs.org/projects/numeroussdk/badge/?version=latest)

Welcome to the repository for `numerous.sdk`!

The `numerous.sdk` which includes all the things you need to build tools and
applications that can run on the [numerous platform](https://numerous.com).

## Requirements

* This project requires python version 3.9 or later.

## Installation

To install `numerous.sdk`
you can use the following command:

```
pip install numerous.sdk
```

## Documentation

Documentation for the numerous SDK can be found at
[readthedocs.io](https://numeroussdk.readthedocs.io). This contains the latest
documentation. We are continuously adding more, as the project matures.

## Contributing

We welcome contributions, but please read [CONTRIBUTING.md](CONTRIBUTING.md)
before you start. It lays down the processes and expectations of contributions
to the numerous SDK.

### Setup development environment

In order to start developing on the numerous SDK, we recommend you create a virtual
environment, and install the package (including `lint` and `test` dependencies) in an
editable state:

```
pip install -e .[lint,test]
```

This will also install `pre-commit` which can then be used to setup the pre-commit
checks, like below:

```
pre-commit install
```

### Generate documentation

In order to generate the documentation, install the requirements, and run the build.

```
cd docs
pip install -r requirements.txt
make html
```

The built documentation is then stored in `docs/build/html`.

## Changes

See the [CHANGELOG.md](CHANGELOG.md) to get an overview latest features, fixes
and other changes to `numerous.sdk`, and also to find the general history of
changes.

## License

`numerous.sdk` is licensed under the MIT License, and it can be read in
[LICENSE.md](LICENSE.txt).

The package is built with the `flit` backend, so it is first necessary to
install this:

```shell
pip install flit
```

Then to install from the top-level directory (containing `pyproject.toml`):

```shell
flit install
```

To run unit tests:

```shell
python -m unittest test.test_qirpass
```

(These take a few minutes to run.)

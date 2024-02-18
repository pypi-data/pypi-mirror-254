# Build wheel

```
pip install wheel
python setup.py bdist_wheel
```

# Build source distribution

```
pip install wheel
python setup.py sdist
```

# Check all is correct with twine

```
pip install twine
twine check dist/*
```

# Upload with twine

Get an API token from PyPi and add the ~/.pypirc as follow:
```
[pypi]
  username = __token__
  password = <TOKEN GOES HERE>
```

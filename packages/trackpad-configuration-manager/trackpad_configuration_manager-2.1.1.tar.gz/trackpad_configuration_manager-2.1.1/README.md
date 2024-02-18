boreas-configurator

## Build package for PyPi
```bash
python .\setup.py sdist   
py -m twine upload dist/*
```
Source: https://packaging.python.org/en/latest/tutorials/packaging-projects/

Other source: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

The package is then available at https://pypi.org/project/trackpad_configuration_manager/

The test package is available at https://test.pypi.org/project/trackpad_configuration_manager/
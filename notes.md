```
virtualenv -p python3 venv
source venv/bin/activate

pip install .
pip install twine build

python -m build
twine upload dist/*
```

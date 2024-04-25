Using [packaging guide from mypy docs](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages).

Full code is
- https://github.com/boxwise/boxtribute/blob/master/back/boxtribute_server/db.py
- https://github.com/boxwise/boxtribute/blob/master/back/boxtribute_server/models/definitions/qr_code.py

### Instructions

Clone repo, create and activate venv.

```sh
pip install -U -e . -r requirements.txt
mypy package_a/
```

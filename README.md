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

This gives the error

```
package_a/qr_code.py:6: error: Name "db.Model" is not defined  [name-defined]
Found 1 error in 1 file (checked 3 source files)
```

How can I fix it?

See also https://github.com/python/typeshed/pull/11731.

Third-party `flask_utils.py` module is [here](https://github.com/coleifer/peewee/blob/master/playhouse/flask_utils.py).

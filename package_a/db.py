from playhouse.flask_utils import FlaskDB


class DatabaseManager(FlaskDB):
    pass


# Shows error below, same when using either of the last lines
# package_a/qr_code.py:6: error: Name "db.Model" is not defined  [name-defined]
db = DatabaseManager()
# db = FlaskDB()
# db: FlaskDB = FlaskDB()

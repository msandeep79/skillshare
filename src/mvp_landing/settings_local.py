import os



SOUTH_DATABASE_ADAPTERS = {
    'default': "south.db.sqlite3"
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE_NAME = os.path.join(BASE_DIR, 'db.sqlite3')             # Or path to database file if using sqlite3.
#DATABASE_USER = 'username'               # Not used with sqlite3.
#DATABASE_PASSWORD = 'password'               # Not used with sqlite3.
DATABASE_ENGINE = 'sqlite3'  #mysql, etc
#DATABASE_HOST = 'localhost'
#DATABASE_PORT = ''
import sqlite3
from contextlib import contextmanager

database = "./grades.db"


@contextmanager
def create_connection(db_file):
    """creates a data base connection to a SQlite database"""

    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()

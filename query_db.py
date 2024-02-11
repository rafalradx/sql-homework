from connect import create_connection, database

with create_connection(database) as conn:
    pass

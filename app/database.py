import os
import pyodbc


def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SecureNotesDB;'
        f'UID={os.getenv("DB_USER")};'
        f'PWD={os.getenv("DB_PASSWORD")};'
    )

    return conn
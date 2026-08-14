import pyodbc

def get_db_connection():
    # Credenciales hardcodeadas (Sensitive Data Exposure)
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SecureNotesDB;'
        'UID=sa;'
        'PWD=Password123!'
    )
    return conn
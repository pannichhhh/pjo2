import psycopg2
from psycopg2 import OperationalError, DatabaseError


class Config : 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:panichakam@localhost/IT_Ledger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname="IT_Ledger",
            user="postgres",
            password="panichakam",
            host="localhost",
            port="5432"
        )

        # check status
        if connection.status == psycopg2.extensions.STATUS_READY:
            print("Connected to the PostgreSQL database.")
            return connection
    except OperationalError as e:
        print("Failed to connect to the database.")
        print(f"Error: {e}")
        return None
    except Exception as e:
        print("Unexpected error occurred.")
        print(f"Error: {e}")
        return None
    
def check_connection_status(connection):
    if connection and connection.closed == 0:
        print("Connection is active.")
    else:
        print("Connection is closed.")


conn = connect_to_database()

if conn:
    check_connection_status(conn)
    # query version
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print(f"Database version: {db_version[0]}")
    except DatabaseError as e:
        print("Error executing query:", e)

    # close connection
    conn.close()
    print("Connection closed.")

"""
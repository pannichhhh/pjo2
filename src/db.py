import psycopg2
from config import Config

def get_db_connection():
    try:
        conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
        return conn
    except Exception as e:
        return f"Error: {str(e)}"

def execute_query(query, params=None):
    try: 
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return f'Fetched data: {rows}'
    except Exception as e:
        return f'Error: {str(e)}'

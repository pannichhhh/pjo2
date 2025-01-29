import psycopg2
from psycopg2 import OperationalError, DatabaseError


class Config : 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:panichakam@localhost/IT_Ledger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


from app import app 
from src.db import execute_query

@app.route('/')
def home():
    return "FLASK"

@app.route('/GETdb')
def index():
    return execute_query('SELECT * FROM "Asset"')
from helpers.utils import app
from src.db import execute_query

@app.route('/')
def home():
    return "TESt SERVER"

@app.route('/GET/FixAsset')
def fixedasset():
    return execute_query('SELECT * FROM "Asset"')


@app.route('/GET/Emp')
def emp():
    return execute_query('SELECT * FROM "EmpDetail"')
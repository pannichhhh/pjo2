#from flask import Flask
from flask import Flask
from src.routes import *



app = Flask(__name__)
        
if __name__ == '__main__':
    app.run(debug=True)

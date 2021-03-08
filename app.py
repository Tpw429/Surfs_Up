# importing flask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
    
# In terminal below, I ran the following to create the link
# set FLASK_APP=app.py
# flask run
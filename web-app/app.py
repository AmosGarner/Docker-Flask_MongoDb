import os, json
from flask import Flask, redirect, url_for, request, render_template, jsonify, Response
from bson import json_util
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

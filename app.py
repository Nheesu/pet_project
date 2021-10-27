from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    return

@app.route('/search/detail', methods=['GET'])
def detail():
    return


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
from flask import Flask, request, render_template
import sqlite3
from crawler import crawl
from database import create_database, index_page, search

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_request():
    query = request.args.get('q')
    results = search(query)
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    create_database()
    app.run(debug=True)

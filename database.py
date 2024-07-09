import sqlite3

def create_database():
    conn = sqlite3.connect('search_engine.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pages
                 (url TEXT, content TEXT)''')
    conn.commit()
    conn.close()

def index_page(url, content):
    conn = sqlite3.connect('search_engine.db')
    c = conn.cursor()
    c.execute("INSERT INTO pages (url, content) VALUES (?, ?)", (url, content))
    conn.commit()
    conn.close()

def search(query):
    conn = sqlite3.connect('search_engine.db')
    c = conn.cursor()
    c.execute("SELECT url, content FROM pages WHERE content LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()
    return results

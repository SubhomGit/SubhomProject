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
    ranked_results = rank_results(query, results)
    return ranked_results

def rank_results(query, results):
    query_words = query.lower().split()
    ranked_results = []

    for url, content in results:
        score = sum(content.lower().count(word) for word in query_words)
        ranked_results.append((url, score))

    ranked_results.sort(key=lambda x: x[1], reverse=True)
    return [(url, score) for url, score in ranked_results if score > 0]

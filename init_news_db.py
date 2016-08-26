import sqlite3

def init_news_db(out_db):
    print("STARTING IMAGE SEARCH, PLEASE WAIT")
    out_c = out_db.cursor()
    out_c.execute('''CREATE TABLE IF NOT EXISTS news
        (title TEXT PRIMARY KEY,
        link TEXT)''')
    out_db.commit()
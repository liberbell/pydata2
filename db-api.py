import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('db-api.db')
    curl = db.cursor()
    print('create')
    cur.execute('DROP TABLE IF EXISTS test')
    cur.execute('''
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        ''')
    print('insert row')
    cur.execute('''
        INSERT INTO test (string, number) VALUES ('one', 1)
        ''')
    print('insert row')
    cur.execute('''
        INSERT INTO test (string, number) VALUES ('two', 2)
        ''')

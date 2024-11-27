import sqlite3

# Inicializar banco de dados e criar tabela Orders
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id TEXT PRIMARY KEY,
            items TEXT NOT NULL,
            status INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
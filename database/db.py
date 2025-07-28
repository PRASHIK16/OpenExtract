# database/db.py

import sqlite3

def create_connection(db_file="data_store.db"):
    conn = sqlite3.connect(db_file)
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS financial_news (
        id INTEGER PRIMARY KEY,
        company TEXT,
        stock_symbol TEXT,
        revenue TEXT,
        net_income TEXT,
        eps TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bank_summary (
        id INTEGER PRIMARY KEY,
        holder TEXT,
        credit TEXT,
        debit TEXT,
        balance TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS upi_summary (
        id INTEGER PRIMARY KEY,
        upi_id TEXT,
        sent TEXT,
        received TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT
    )
    ''')

    conn.commit()

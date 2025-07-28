# analysis/aggregator.py

import sqlite3

def get_total_expense_and_income(db_file="data_store.db"):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("SELECT SUM(CAST(REPLACE(credit, '₹', '') AS REAL)) FROM bank_summary")
    total_credit = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(CAST(REPLACE(debit, '₹', '') AS REAL)) FROM bank_summary")
    total_debit = cur.fetchone()[0] or 0

    return {
        "Total Credit": total_credit,
        "Total Debit": total_debit,
        "Net Savings": total_credit - total_debit
    }

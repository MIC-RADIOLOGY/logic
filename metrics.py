import sqlite3
import pandas as pd

DB_PATH = "metrics.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            fixture_id INTEGER PRIMARY KEY,
            date TEXT,
            league TEXT,
            predicted_winner TEXT,
            actual_winner TEXT,
            correct INTEGER
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(fixture_id, date, league, predicted_winner, actual_winner=None):
    correct = 1 if predicted_winner == actual_winner else 0 if actual_winner else None
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        INSERT OR REPLACE INTO predictions 
        (fixture_id, date, league, predicted_winner, actual_winner, correct)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (fixture_id, date, league, predicted_winner, actual_winner, correct))
    conn.commit()
    conn.close()

def get_accuracy_by_league():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT league, AVG(correct) as accuracy 
        FROM predictions 
        WHERE correct IS NOT NULL
        GROUP BY league
    """, conn)
    conn.close()
    return df

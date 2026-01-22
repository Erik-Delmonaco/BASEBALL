import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
df = pd.read_csv('Batting.csv')
df.to_sql('Batting', conn, if_exists = 'replace', index = False)
conn.commit()
conn.close()
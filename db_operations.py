import psycopg2
from db_queries import *
from datetime import datetime


#____________________________________ Database functions ____________________________________

def db_connection():
    try:
        connection = psycopg2.connect(
            dbname="defaultdb",
            user="avnadmin",
            password="AVNS_jj25SnhUAlU7PzpfngP",
            host="pg-1707b0b5-learning-tracker.b.aivencloud.com",  
            port="23944"
        )
    except Exception as e:
        print(f"Error in database connection: {e}")
    return connection

def selectTableRows(query):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def selectTableRow(query, *params):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchone()
    cur.close()
    conn.close()
    return rows

def insertUpdateDeleteRow(query, *params):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, params)  
    conn.commit()
    cur.close()
    conn.close()
    

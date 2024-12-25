import psycopg2
from db_queries import *
from datetime import datetime


# ____________________________________
# common functions
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

def getTableRows(query):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insertIntoTable(query):
    # Add your insert logic here
    return

# ____________________________________
# get functions

def getLearnigEntries():
    rows = getTableRows(ALL_LEARNING_ENTRIES)
    return rows

def getSubjects():
    rows = getTableRows(ALL_SUBJECTS)
    return rows

# ____________________________________
# insert functions
 
def addTableRows(query, data): #Here you have to passs the query and data parameter
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, data)  
    conn.commit()
    cur.close()
    conn.close()

def addLearnigEntries(date, learning): #Here u dont need to pass query as it will be executed 
    query = ADD_LEARNING_ENTRIES
    data = (date, learning)
    addTableRows(query, data)
    return {"message": "Entry added successfully!"}  # Return a success message



# ____________________________________
# update functions



# ____________________________________
# delete functions
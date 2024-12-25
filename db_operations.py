import psycopg2
from db_queries import *
from datetime import datetime


#____________________________________ common functions ____________________________________

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

def selectTableRow(query, id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, (id,))
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

#____________________________________ select functions ____________________________________

def selectLearnigEntryDetails(id):  
    row = selectTableRow(LEARNING_ENTRY, id)
    final_data = {
                    'id': row[0],
                    'date': row[1],
                    'learning': row[2]
                }
    return final_data

def selectLearnigEntries():  
    rows = selectTableRows(ALL_LEARNING_ENTRIES)
    final_data = []
    for (id, date, learning) in rows:
        item = {
                    'id': id,
                    'date': date,
                    'learning': learning,
                }
        final_data.append(item)
    return final_data

def selectSubjectDetails(id):  
    row = selectTableRow(SUBJECT, id)
    final_data = {
                    'id': row[0],
                    'name': row[1],
                    'optional': row[2],
                    'description': row[3],
                }
    return final_data

def selectSubjects():
    rows = selectTableRows(ALL_SUBJECTS)
    final_data = []
    for (id, name, optional, description) in rows:
        item = {
                    'id': id,
                    'name': name,
                    'optional': optional,
                    'description': description,
                }
        final_data.append(item)
    return final_data


#____________________________________ insert functions ____________________________________
def insertLearningEntry(date, learning):  
    insertUpdateDeleteRow(INSERT_LEARNING_ENTRY, date, learning)

def insertSubject(name, optional, description): 
    insertUpdateDeleteRow(INSERT_SUBJECT, name, optional, description)


#____________________________________ update functions ____________________________________
def updateLearningEntry(id, date, learning):
    insertUpdateDeleteRow(UPDATE_LEARNING_ENTRY, date, learning, id)
    
def updateSubject(id, name, optional, description):
    insertUpdateDeleteRow(UPDATE_SUBJECT, name, optional, description, id)

#____________________________________ delete functions ____________________________________
def deleteLearningEntry(id):
    insertUpdateDeleteRow(DELETE_LEARNING_ENTRY, id)
    
def deleteLearningEntries():
    insertUpdateDeleteRow(ALL_DELETE_LEARNING_ENTRIES)    
    
def deleteSubject(id):
    insertUpdateDeleteRow(DELETE_SUBJECT, id)
    
def deleteSubjects():
    insertUpdateDeleteRow(ALL_DELETE_SUBJECTS)     
#____________________________________ Testing only____________________________________
# Only runs when executed directly
# if __name__ == "__main__":    
#     insertLearningEntry('2024-11-25', 'Clean code practice')
#     insertSubject('Computer', True, 'Learning is Fun')

#     insertLearningEntry('2024-11-25', 'Saaf code practice')
#     insertSubject('Computer', True, 'Seekhna is Fun')
    # updateLearningEntry('2024-11-25', 'Yes learnt Clean code practice', 33)
    # updateSubject('English', True, 'Wow Learning is Fun', 9)
    
    # deleteLearningEntry(32)
    # deleteSubject(9)
    
    # deleteSubjects()
    # deleteLearningEntries()
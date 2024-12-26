from db_operations import *

#____________________________________ select functions ____________________________________

def selectLearnigEntryDetails(id):  
    row = selectTableRow(LEARNING_ENTRY, id)
    
    if row == None:
        return {"error":"Invalid id."}
    
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
    
    if row == None:
        return {"msg":"Invalid id."}
    
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
def doesEntryExists(id, table_name):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s;"
    result = selectTableRow(query, id)
    return result[0] > 0 

def updateLearningEntry(id, date, learning):
    insertUpdateDeleteRow(UPDATE_LEARNING_ENTRY, date, learning, id)
      
def updateSubject(id, name, optional, description):
    insertUpdateDeleteRow(UPDATE_SUBJECT, name, optional, description, id)


#____________________________________ delete functions ____________________________________
def doesEntryExists(id, table_name):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s;"    
    if isinstance(id, (str, int)):
        result = selectTableRow(query, id)
        return result[0] > 0
    
def deleteLearningEntry(id):
        print(f"Executing delete for ID {id}")
        insertUpdateDeleteRow(DELETE_LEARNING_ENTRY, id)

def deleteLearningEntries():
    insertUpdateDeleteRow(ALL_DELETE_LEARNING_ENTRIES)    
    
def deleteSubject(id):
    row = insertUpdateDeleteRow(DELETE_SUBJECT, id)
    if row == None:
        return {"msg":"Invalid id."}
    
    final_data = {
                    'id': row[0],
                    'name': row[1],
                    'optional': row[2],
                    'description': row[3],
                }
    return final_data
    
def deleteSubjects():
    insertUpdateDeleteRow(ALL_DELETE_SUBJECTS)     
#____________________________________ Testing only____________________________________
# Only runs when executed directly
# if __name__ == "__main__":    

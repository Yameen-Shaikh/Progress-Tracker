from flask import Flask, jsonify, request
from db_operations import *

app = Flask(__name__)


#________________________________ GET | DELETE HTTP methods _______________________________________


@app.route('/learning/<string:param>', methods = ["GET", "DELETE"])
def getPutDeleteLearning(param):
    if request.method == "GET" and param == 'all':
        result = selectLearnigEntries()
    
    if request.method == "GET" and param != 'all':    
        result = selectLearnigEntryDetails(param)

    if request.method == "DELETE" and param == 'all':
        result = deleteLearningEntries()
    
    if request.method == "DELETE" and param != 'all':
        result = deleteLearningEntry(param)

    return (jsonify(result))


@app.route('/subject/<string:param>', methods = ["GET", "DELETE"])
def getPutDeleteSubject(param):
    if request.method == "GET" and param == 'all':
        result = selectSubjects()
    
    if request.method == "GET" and param != 'all':    
        result = selectSubjectDetails(param)

    if request.method == "DELETE" and param == 'all':
        result = deleteSubjects()
    
    if request.method == "DELETE" and param != 'all':
        result = deleteSubject(param)

    return (jsonify(result))


#________________________________ POST | PUT HTTP methods _______________________________________


@app.route('/learning/<string:id>', methods = ["POST", "PUT"])
def postPutLearning(id):
    
    data = request.get_json() 
    date = data.get("date")  
    learning = data.get("learning")
      
    if request.method == "POST":
        result = insertLearningEntry(date, learning)
        
    if request.method == "PUT":    
        result = updateLearningEntry(id, date, learning)

    return (jsonify(result))

@app.route('/subject/<string:id>', methods = ["POST", "PUT"])
def postPutSubject(id):
    
    data = request.get_json() 
    name = data.get("name")  
    optional = data.get("optional")
    description = data.get("description")

    if request.method == "POST":
        result = insertSubject(name, optional, description)
        
    if request.method == "PUT":    
        result = updateSubject(id, name, optional, description)

    # return (f"Successfully updated ✅ {data}") 
    return (jsonify(result))

#______________________________________________________________________________________________
if __name__ == '__main__': 
    app.run(debug=True)
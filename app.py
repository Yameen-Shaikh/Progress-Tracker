from flask import Flask, jsonify, request
from data_processor import *


app = Flask(__name__)


#________________________________ GET | DELETE HTTP methods _______________________________________

@app.route('/learning/', defaults={'param': None}, methods=["GET", "DELETE"])

@app.route('/learning/<string:param>', methods = ["GET", "DELETE"])
def getPutDeleteLearning(param):
    
    if param == None:
        return jsonify({"error": "Parameter all or id is required and cannot be empty."}), 400
    
    if request.method == "GET" and param == 'all':
        result = selectLearnigEntries()
    
    if request.method == "GET" and param != 'all':    
        result = selectLearnigEntryDetails(param)
        
    if request.method == "DELETE" and param == 'all':
        result = deleteLearningEntries()
        return "All learnings deleted! 🫣"
        
    if request.method == "DELETE" and param != 'all':
        if not doesEntryExists(param, "learning_entries"):
            return jsonify({"error": "ID does not exist."}), 404
        
        deleteLearningEntry(param)
        return "Deleted successfully! 🤗"
        
    return jsonify(result)

@app.route('/subject/', defaults={'param': None}, methods=["GET", "DELETE"])
@app.route('/subject/<string:param>', methods = ["GET", "DELETE"])
def getPutDeleteSubject(param):
    if request.method == "GET" and param == 'all':
        result = selectSubjects()
    
    if request.method == "GET" and param != 'all':    
        result = selectSubjectDetails(param)

    if request.method == "DELETE" and param == 'all':
        result = deleteSubjects()
        return "All subjects deleted! 🫣"
    
    if request.method == "DELETE" and param != 'all':
        if not doesEntryExists(param, "subjects"):
            return jsonify({"error": "ID does not exist."}), 404
        result = deleteSubject(param)
        return "Deleted successfully! 🤗"
    
    return jsonify(result)


#________________________________ POST | PUT HTTP methods _______________________________________

@app.route('/learning/', defaults={'id': None}, methods=["POST", "PUT"])
@app.route('/learning/<string:id>', methods=["POST", "PUT"])

def postPutLearning(id):
    data = request.get_json() 
    date = data.get("date")  
    learning = data.get("learning")
    
    if request.method == "POST":
        result = insertLearningEntry(date, learning)
        return "Added successfully! 😀"
        
    if request.method == "PUT":
        if not doesEntryExists(id, "learning_entries"):  
                return jsonify({"error": f"Learning entry with ID {id} does not exist."}), 404
            
        # Proceed with the update if ID exists
        result = updateLearningEntry(id, date, learning)
        return jsonify({"message": f"Successfully updated entry with ID {id} ✅", "data": data})        
    return jsonify({"error": "Invalid request."}), 400
 
@app.route('/subject/', defaults={'id': None}, methods=["POST", "PUT"])
@app.route('/subject/<string:id>', methods = ["POST", "PUT"])

def postPutSubject(id):
    data = request.get_json() 
    name = data.get("name")  
    optional = data.get("optional")
    description = data.get("description")

    if request.method == "POST":
        result = insertSubject(name, optional, description)
        return "Subject added successfully! 😀"
        
    if request.method == "PUT":    
        if not doesEntryExists(id, "subjects"):  
            return jsonify({"error": f"Learning entry with ID {id} does not exist."}), 404
            
        result = updateSubject(id, name, optional, description)
        return jsonify({"message": f"Successfully updated entry with ID {id} ✅", "data": data})    
    return jsonify({"error": "Invalid request."}), 400    


#______________________________________________________________________________________________
if __name__ == '__main__': 
    app.run(debug=True)
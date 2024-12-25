from flask import Flask, jsonify, request
from datetime import datetime
from db_queries import *
from db_operations import *


app = Flask(__name__)

# ____________________________________
# get HTTP method

@app.route("/")
def root():
    return "Welcome to the app! Visit /learning/entries for more."


@app.route('/learning/entries')
def get_Learnig_Entries():
    data = getLearnigEntries()
    return jsonify(data)

@app.route('/subjects')
def get_Subjects():
    subject = getSubjects()
    return jsonify(subject)

 
# ____________________________________
# post HTTP method

@app.route('/add/learning', methods=['POST'])
def add_learnings():
    data = request.get_json() #Here the get the data by post and in json
    date = data.get("date")  
    learning = data.get("learning")  

    if not date or not learning:
        return jsonify({"error": "Missing data!"})  # Return an error if data is missing
    
    add = addLearnigEntries(date, learning)
    return jsonify(add)








if __name__ == '__main__': 
    app.run(debug=True) 

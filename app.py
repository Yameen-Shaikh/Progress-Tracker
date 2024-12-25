from flask import Flask, jsonify, request
from db_queries import *
from db_operations import *

app = Flask(__name__)

#________________________________ GET & POST HTTP methods _______________________________________

@app.route('/learning', methods = ["GET", "POST"])
def getPostLearning():
    if request.method == "GET":
        data = getLearnigEntries()
        return jsonify(data)   
     
    #post
    data = request.get_json() #Here the get the data by post and in json
    date = data.get("date")  
    learning = data.get("learning")  

    if date and learning:
        add = addLearnigEntries(date, learning)
        return jsonify(add) 
    
    return jsonify({"error": "Missing data!"})  # Return an error if data is missing
    
#________________________________ PUT & DELTE HTTP methods _______________________________________


if __name__ == '__main__': 
    app.run(debug=True) 

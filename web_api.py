#make a website 
import flask 
from flask import request, jsonify
import student_generator_v2 as sg

#create a flask app 
app = flask.Flask(__name__)

#Use student generator as a base
# Get student dictionaries
# Create 2 routes
#  Return all students 
# Return students by major

#Auto reload server when changes are made
app.config["DEBUG"] = True 

#Get the student dictionaries 
student_dictionaries = sg.get_student_dictionaries()



#create a route(page in our application) for the server home page
@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello World, My name is Karyna Lopez</h1>"


#create a route to return all student data in json format
@app.route('/api/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)
app.run()

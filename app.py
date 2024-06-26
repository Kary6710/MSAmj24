#Brooooo Impoort: module
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#Make a flask app
app = Flask(__name__)
app.config["DEBUG"]

#Set a secret key to iuse when validating form data
app.config["SECRET_KEY"] = "your secret key"

#Function to request students data from the api
#Input: url
#output: JSON student data
def get_student_data(url):
    #make a request 
    response = requests.get(url)

    #convert format to json
    response_json = response.json()
    
    return response_json

#create a routes Wfor the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #Get the student data 
    #Make a request to the student data api url
    url = "http://127.0.0.1:5000/api/students/all"

    student_data = get_student_data(url)

    #send the student data to the index.html page
    
    return render_template('index.html')


app.run(port = 5005)

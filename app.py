# Impoort: module
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#Make a flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#Set a secret key to iuse when validating form data
app.config["SECRET_KEY"] = "your secret key"

#efine a constant value for url 
URL= "http://127.0.0.1:5000/api/students/all"


#Function to request students data from the api
#Input: url
#output: JSON student data
def get_student_data(URL):
    #make a request 
    response = requests.get(URL)

    #convert format to json
    response_json = response.json()
    
    return response_json

#function to return a list of unique majors 
#input: url 
#Output: list of unique majors 
def get_unique_majors(URL):
    
     #get a list of students from the student api 

    student_list = get_student_data(URL)

    #produce a list of unique majors
    unique_majors = []
    
    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])

    unique_majors.sort()
    return unique_majors

#create a routes Wfor the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #Get the student data 
    #Make a request to the student data api url

    student_data = get_student_data(URL)

    #send the student data to the index.html page
    
    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    #write code that gets a unique list of majors from student data 
    major_list = get_unique_majors()
    #get student data rom the api: list of student dictionaries

    return render_template('majors.html', major_list = major_list)
    
@app.route('/majors', methods=['POST'])



def majors_post():
    result_list = []
    major_list= get_unique_majors()
    
    #get the form data that was submitted 
    major = request.form.get('major')
    #validate our form data. If invalid form data. show erro message
    if not major:
        flash("You must select a major")
    else: 
        #otherwise find students with the selected major and return to the majors.html page
        #Get the student data
        
        student_list = get_student_data(URL)
        
        #loop through list of students. If studnets major == mjaor. place student in a result list
        for student in student_list:
            if student['major'] == major: 
                result_list.append(student)
        
        #send teh result list to the majors.html page

    return render_template('majors.html', major_list = major_list, result_list=result_list)

app.run(port = 5005)

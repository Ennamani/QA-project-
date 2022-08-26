from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from schema import *

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

d = SQLAlchemy(application)


@application.route('/')
def home_page():
    return render_template('home.html')


@application.route('/about')
def about_page():
    return render_template('about.html')


@application.route('/contact')
def contact_page():
    return render_template('contact.html')


@application.route('/education')
def education_page():
    return render_template('education.html')

@application.route('/colleges')
def task_page():
    all_colleges = Colleges.query.all()
    return render_template('colleges.html', list_of_names=all_colleges)

@application.route('/colleges/<int:id>')
def programslist(id):
    program_of_specific_college = Programs.query.filter_by(college_id=id)
    college = Colleges.query.get(id)
    return render_template('programs.html',list_of_names=program_of_specific_college,college=college)

@application.route('/students/<int:id>/')
def studentslist(id):
    student_of_specific_program = Students.query.filter_by(program_id=id)
    program = Programs.query.get(id)
    return render_template('students.html',list_of_names=student_of_specific_program,program=program)


if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8060)

# Run web server using this file
# @application.route('/colleges/<int:id>')
# def programslist(id):
#     program_of_specific_college = Programs.query.filter_by(college_id=id)
#     college = Colleges.query.get(id)
#     return render_template('programs.html',list_of_names=program_of_specific_college,college=college)

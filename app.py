from flask import Flask, redirect, url_for, render_template



app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/education')
def education_page():
    return render_template('education.html')

@app.route('/colleges')
def task_page():
    all_colleges = Colleges.query.all()
    return render_template('colleges.html', list_of_names=all_colleges)

@app.route('/colleges/<int:id>')
def programslist(id):
    program_of_specific_college = Programs.query.filter_by(college_id=id)
    college = Colleges.query.get(id)
    return render_template('programs.html',list_of_names=program_of_specific_college,college=college)

@app.route('/students/<int:id>/')
def studentslist(id):
    student_of_specific_program = Students.query.filter_by(program_id=id)
    program = Programs.query.get(id)
    return render_template('students.html',list_of_names=student_of_specific_program,program=program)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8060)
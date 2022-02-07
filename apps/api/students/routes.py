from flask import render_template, redirect, request, url_for

from apps import db
from flask_login import login_required
from apps.api.students import blueprint

from apps.api.students.model import Student


@blueprint.route('/students', methods=['GET'])
@login_required
def students():
    records_student = Student.query.all()
    print(records_student)

    return render_template('students/students.html')


@blueprint.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_students():
    if request.method == 'GET':
        return render_template('students/student-info.html')
    if request.method == 'POST':
        # print(request.form)
        # print(request.files)
        avatar = request.files['avatar']
        code = request.form['code']
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        birthday = request.form['birthday']
        email = request.form['email']
        phone_number = request.form['phone_number']
        identify_card = request.form['identify_card']
        bhyt = request.form['bhyt']
        student_class = request.form['class']
        student_major = request.form['major']
        print(avatar)
        # return
        return render_template('students/student-info.html')
    # return render_template('students/student-info.html')

import traceback
import pandas as pd
from datetime import datetime

from flask_login import login_required
from flask import render_template, request, redirect

from apps import db
from apps.api.students import blueprint
from apps.api.students.model import Student

from apps.core.upload_file import upload_file


@blueprint.route('/students', methods=['GET'])
@login_required
def students():
    records_student = Student.query.filter(
        Student.deleted==False).all()

    return render_template('students/students.html', student=records_student, segment='students')


@blueprint.route('/import-student', methods=['POST'])
@login_required
def import_student():
    if request.method == 'POST':
        df = pd.read_csv('advanced_python.csv', sep=';')

        try:
            list_student = []
            for data in df.values:
                print(data[4])
                code = data[1]
                name = data[2] + ' ' + data[3]
                birthday = datetime.strptime(data[4], '%m/%d/%Y')
                student_class = data[5].replace(' ', '')

                record_student = Student()
                record_student.code = code
                record_student.name = name
                record_student.birthday = birthday
                record_student.student_class = student_class

                list_student.append(record_student)

            db.session.add_all(list_student)
            db.session.commit()

            return redirect('/students')
        except Exception as e:
            print(traceback.format_exc())
            return render_template('students/students.html', has_error='Import failed!', segment='students')


@blueprint.route('/add-student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'GET':
        return render_template('students/student-info.html', segment='students')

    if request.method == 'POST':
        avatar = request.files['avatar']
        code = request.form['code']
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        birthday = request.form['birthday']
        email = request.form['email']
        phone_number = request.form['phone_number']
        identification = request.form['identification']
        health_insurance = request.form['health_insurance']
        student_class = request.form['student_class']
        student_major = request.form['student_major']

        if not code:
            return render_template('students/student-info.html', has_error='Code is empty!', segment='students')
        if not name:
            return render_template('students/student-info.html', has_error='Name is empty!', segment='students')
        if not address:
            return render_template('students/student-info.html', has_error='Address is empty!', segment='students')
        if not gender:
            return render_template('students/student-info.html', has_error='Gender is empty!', segment='students')
        if not birthday:
            return render_template('students/student-info.html', has_error='Birthday is empty!', segment='students')
        if not email:
            return render_template('students/student-info.html', has_error='Email is empty!', segment='students')
        if not phone_number:
            return render_template('students/student-info.html', has_error='Phone number is empty!', segment='students')
        if not student_class:
            return render_template('students/student-info.html', has_error='Class is empty!', segment='students')
        if not student_major:
            return render_template('students/student-info.html', has_error='Major is empty!', segment='students')

        record_student = Student.query.filter(
            Student.code == code).filter(
            Student.deleted == False).first()
        if record_student:
            return render_template('students/student-info.html', has_error='Student code already exists!', segment='students')

        record_student = Student.query.filter(
            Student.email == email).filter(
            Student.deleted == False).first()
        if record_student:
            return render_template('students/student-info.html', has_error='Student email already exists!', segment='students')
        try:
            if avatar:
                avatar = upload_file(avatar)
            else:
                avatar = "static/assets/images/avatar.png"

            record_student = Student(**request.form)
            record_student.avatar = avatar
            db.session.add(record_student)
            db.session.commit()

            return redirect('/students')
        except Exception as e:
            print(traceback.format_exc())
            return render_template('students/student-info.html', has_error='Error!', segment='students')


@blueprint.route('/info-student/<id>', methods=['GET', 'POST'])
@login_required
def student_info(id):
    if request.method == 'GET':
        record_student = Student.query.filter(
            Student.id == id).filter(
            Student.deleted == False).first()

        return render_template('students/student-info.html', student=record_student, segment='students')

    if request.method == 'POST':
        avatar = request.files['avatar']
        code = request.form['code']
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        birthday = request.form['birthday']
        email = request.form['email']
        phone_number = request.form['phone_number']
        identification = request.form['identification']
        health_insurance = request.form['health_insurance']
        student_class = request.form['student_class']
        student_major = request.form['student_major']

        if not code:
            return render_template('students/student-info.html', has_error='Code is empty!', segment='students')
        if not name:
            return render_template('students/student-info.html', has_error='Name is empty!', segment='students')
        if not address:
            return render_template('students/student-info.html', has_error='Address is empty!', segment='students')
        if not gender:
            return render_template('students/student-info.html', has_error='Gender is empty!', segment='students')
        if not birthday:
            return render_template('students/student-info.html', has_error='Birthday is empty!', segment='students')
        if not email:
            return render_template('students/student-info.html', has_error='Email is empty!', segment='students')
        if not phone_number:
            return render_template('students/student-info.html', has_error='Phone number is empty!', segment='students')
        if not student_class:
            return render_template('students/student-info.html', has_error='Class is empty!', segment='students')
        if not student_major:
            return render_template('students/student-info.html', has_error='Major is empty!', segment='students')

        record_student = Student.query.filter(
            Student.id == id).filter(
            Student.deleted == False).first()

        record_student_code = Student.query.filter(
            Student.id != id).filter(
            Student.code == code).filter(
            Student.deleted == False).first()
        if record_student_code:
            return render_template('students/student-info.html', student=record_student, has_error='Student code already exists!', segment='students')

        record_student_email = Student.query.filter(
            Student.id != id).filter(
            Student.email == email).filter(
            Student.deleted == False).first()
        if record_student_email:
            return render_template('students/student-info.html', student=record_student, has_error='Student email already exists!', segment='students')

        if avatar:
            avatar = upload_file(avatar)
        else:
            avatar = "static/assets/images/avatar.png"
        record_student.code = code
        record_student.name = name
        record_student.email = email
        record_student.address = address
        record_student.gender = gender
        record_student.birthday = birthday
        record_student.phone_number = phone_number
        record_student.identification = identification
        record_student.health_insurance = health_insurance
        record_student.student_class = student_class
        record_student.student_major = student_major
        db.session.commit()

        return render_template('students/student-info.html', student=record_student, segment='students')


@blueprint.route('/student/<id>')
@login_required
def student_delete(id):
    record_student = Student.query.filter(
        Student.id == id).filter(
        Student.deleted == False).first()
    record_student.deleted = True
    db.session.commit()
    return redirect('/students')

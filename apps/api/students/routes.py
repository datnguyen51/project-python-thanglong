from flask import render_template, redirect, request, url_for

from apps import db
from flask_login import login_required
from apps.api.students import blueprint

from apps.api.students.model import Student


@blueprint.route('/students', methods=['GET'])
@login_required
def students():
    records_student = Student.query.all()
    print(records_student[0].id)

    return render_template('students/students.html', student=records_student)


@blueprint.route('/add-student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'GET':
        return render_template('students/student-info.html')

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
            return render_template('students/student-info.html', has_error='Code is empty!')
        if not name:
            return render_template('students/student-info.html', has_error='Name is empty!')
        if not address:
            return render_template('students/student-info.html', has_error='Address is empty!')
        if not gender:
            return render_template('students/student-info.html', has_error='Gender is empty!')
        if not birthday:
            return render_template('students/student-info.html', has_error='Birthday is empty!')
        if not email:
            return render_template('students/student-info.html', has_error='Email is empty!')
        if not phone_number:
            return render_template('students/student-info.html', has_error='Phone number is empty!')
        if not student_class:
            return render_template('students/student-info.html', has_error='Class is empty!')
        if not student_major:
            return render_template('students/student-info.html', has_error='Major is empty!')

        record_student = Student.query.filter_by(
            code=code).filter_by(
            deleted=False).first()

        if record_student:
            return render_template('students/student-info.html', has_error='Student code already exists!')

        record_student = Student.query.filter_by(
            email=email).filter_by(
            deleted=False).first()

        if record_student:
            return render_template('students/student-info.html', has_error='Student email already exists!')

        record_student = Student(**request.form)
        db.session.add(record_student)
        db.session.commit()

        return render_template('students/student-info.html')
    # return render_template('students/student-info.html')


@blueprint.route('/info-student/<id>', methods=['GET', 'PUT'])
@login_required
def student_info(id):
    if request.method == 'GET':
        record_student = Student.query.filter_by(
            id=id).filter_by(
            deleted=False).first()

        # if not record_student:

        return render_template('students/student-info.html', student=record_student)

    if request.method == 'PUT':
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
            return render_template('students/student-info.html', has_error='Code is empty!')
        if not name:
            return render_template('students/student-info.html', has_error='Name is empty!')
        if not address:
            return render_template('students/student-info.html', has_error='Address is empty!')
        if not gender:
            return render_template('students/student-info.html', has_error='Gender is empty!')
        if not birthday:
            return render_template('students/student-info.html', has_error='Birthday is empty!')
        if not email:
            return render_template('students/student-info.html', has_error='Email is empty!')
        if not phone_number:
            return render_template('students/student-info.html', has_error='Phone number is empty!')
        if not student_class:
            return render_template('students/student-info.html', has_error='Class is empty!')
        if not student_major:
            return render_template('students/student-info.html', has_error='Major is empty!')

        record_student = Student.query.filter_by(
            code=code).filter_by(
            deleted=False).first()

        if record_student:
            return render_template('students/student-info.html', has_error='Student code already exists!')

        record_student = Student.query.filter_by(
            email=email).filter_by(
            deleted=False).first()

        if record_student:
            return render_template('students/student-info.html', has_error='Student email already exists!')

        record_student = Student.query.filter_by(
            id=id).filter_by(
            deleted=False).first()

        # db.session.add(record_student)
        db.session.commit()

        return render_template('students/student-info.html')

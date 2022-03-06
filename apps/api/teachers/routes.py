import traceback

from flask_login import login_required
from flask import render_template, request, redirect

from apps import db
from apps.api.teachers import blueprint
from apps.api.teachers.model import Teacher

from apps.core.upload_file import upload_file


@blueprint.route('/teachers', methods=['GET'])
@login_required
def teachers():
    records_teacher = Teacher.query.filter(
        Teacher.deleted==False).all()

    return render_template('teachers/teachers.html', teacher=records_teacher, segment='teachers')


@blueprint.route('/add-teacher', methods=['GET', 'POST'])
@login_required
def add_teacher():
    if request.method == 'GET':
        return render_template('teachers/teacher-info.html', segment='teachers')

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
        teacher_major = request.form['teacher_major']

        if not code:
            return render_template('teachers/teacher-info.html', has_error='Code is empty!', segment='teachers')
        if not name:
            return render_template('teachers/teacher-info.html', has_error='Name is empty!', segment='teachers')
        if not address:
            return render_template('teachers/teacher-info.html', has_error='Address is empty!', segment='teachers')
        if not gender:
            return render_template('teachers/teacher-info.html', has_error='Gender is empty!', segment='teachers')
        if not birthday:
            return render_template('teachers/teacher-info.html', has_error='Birthday is empty!', segment='teachers')
        if not email:
            return render_template('teachers/teacher-info.html', has_error='Email is empty!', segment='teachers')
        if not phone_number:
            return render_template('teachers/teacher-info.html', has_error='Phone number is empty!', segment='teachers')
        if not teacher_major:
            return render_template('teachers/teacher-info.html', has_error='Major is empty!', segment='teachers')

        record_teacher = Teacher.query.filter(
            Teacher.code == code).filter(
            Teacher.deleted == False).first()

        if record_teacher:
            return render_template('teachers/teacher-info.html', has_error='Teacher code already exists!', segment='teachers')

        record_teacher = Teacher.query.filter(
            Teacher.email == email).filter(
            Teacher.deleted == False).first()

        if record_teacher:
            return render_template('teachers/teacher-info.html', has_error='Teacher email already exists!', segment='teachers')
        try:
            if avatar:
                avatar = upload_file(avatar)
            else:
                avatar = "static/assets/images/avatar.png"

            record_teacher = Teacher(**request.form)
            record_teacher.avatar = avatar
            db.session.add(record_teacher)
            db.session.commit()

            return redirect('/teachers')
        except Exception as e:
            print(traceback.format_exc())
            return render_template('teachers/teacher-info.html', has_error='Error!', segment='teachers')


@blueprint.route('/info-teacher/<id>', methods=['GET', 'POST'])
@login_required
def teacher_info(id):
    if request.method == 'GET':
        record_teacher = Teacher.query.filter(
            Teacher.id == id).filter(
            Teacher.deleted == False).first()

        return render_template('teachers/teacher-info.html', teacher=record_teacher, segment='teachers')

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
        teacher_major = request.form['teacher_major']

        if not code:
            return render_template('teachers/teacher-info.html', has_error='Code is empty!', segment='teachers')
        if not name:
            return render_template('teachers/teacher-info.html', has_error='Name is empty!', segment='teachers')
        if not address:
            return render_template('teachers/teacher-info.html', has_error='Address is empty!', segment='teachers')
        if not gender:
            return render_template('teachers/teacher-info.html', has_error='Gender is empty!', segment='teachers')
        if not birthday:
            return render_template('teachers/teacher-info.html', has_error='Birthday is empty!', segment='teachers')
        if not email:
            return render_template('teachers/teacher-info.html', has_error='Email is empty!', segment='teachers')
        if not phone_number:
            return render_template('teachers/teacher-info.html', has_error='Phone number is empty!', segment='teachers')
        if not teacher_major:
            return render_template('teachers/teacher-info.html', has_error='Major is empty!', segment='teachers')

        record_teacher = Teacher.query.filter(
            Teacher.id == id).filter(
            Teacher.deleted == False).first()

        record_teacher_code = Teacher.query.filter(
            Teacher.id != id).filter(
            Teacher.code == code).filter(
            Teacher.deleted == False).first()
        if record_teacher_code:
            return render_template('teachers/teacher-info.html', teacher=record_teacher, has_error='Teacher code already exists!', segment='teachers')

        record_teacher_email = Teacher.query.filter(
            Teacher.id != id).filter(
            Teacher.email == email).filter(
            Teacher.deleted == False).first()
        if record_teacher_email:
            return render_template('teachers/teacher-info.html', teacher=record_teacher, has_error='Teacher email already exists!', segment='teachers')

        if avatar:
            avatar = upload_file(avatar)
        else:
            avatar = "static/assets/images/avatar.png"
        record_teacher.code = code
        record_teacher.name = name
        record_teacher.email = email
        record_teacher.address = address
        record_teacher.gender = gender
        record_teacher.birthday = birthday
        record_teacher.phone_number = phone_number
        record_teacher.identification = identification
        record_teacher.health_insurance = health_insurance
        record_teacher.teacher_major = teacher_major
        db.session.commit()

        return render_template('teachers/teacher-info.html', teacher=record_teacher, segment='teachers')


@blueprint.route('/teacher/<id>')
@login_required
def teacher_delete(id):
    record_teacher = Teacher.query.filter(
        Teacher.id == id).filter(
        Teacher.deleted == False).first()
    record_teacher.deleted = True
    db.session.commit()
    return redirect('/teachers')

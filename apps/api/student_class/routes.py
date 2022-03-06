import traceback

from flask_login import login_required
from flask import render_template, request, redirect

from apps import db
from apps.api.student_class import blueprint
from apps.api.students.model import Student
from apps.api.teachers.model import Teacher
from apps.api.student_class.model import StudentClass


@blueprint.route('/class', methods=['GET'])
@login_required
def students_class():
    records_class = StudentClass.query.filter(
        StudentClass.deleted == False).all()

    return render_template('student_class/class.html', student_class=records_class, segment='class')


@blueprint.route('/add-class', methods=['GET', 'POST'])
@login_required
def add_class():
    if request.method == 'GET':
        records_student = Student.query.filter(
            Student.deleted == False).all()

        records_teacher = Teacher.query.filter(
            Teacher.deleted == False).all()

        return render_template('student_class/class-info.html', student=records_student, teacher=records_teacher, segment='class')

    if request.method == 'POST':
        code = request.form.get('code')
        name = (request.form.get('name')).replace(',', " ")
        teacher = request.form.get('teacher')
        student = list(request.form.get('student').split(','))

        records_student = Student.query.filter(
            Student.deleted == False).all()

        records_teacher = Teacher.query.filter(
            Teacher.deleted == False).all()

        if not code:
            return render_template('student_class/class-info.html', has_error='Code is empty!', student=records_student, teacher=records_teacher, segment='class')
        if not name:
            return render_template('student_class/class-info.html', has_error='Name is empty!', student=records_student, teacher=records_teacher, segment='class')
        if not teacher:
            return render_template('student_class/class-info.html', has_error='Teacher is empty!', student=records_student, teacher=records_teacher, segment='class')

        record_class = StudentClass.query.filter(
            StudentClass.code == code).filter(
            StudentClass.deleted == False).first()
        if record_class:
            return render_template('student_class/class-info.html', has_error='Class code already exists!', student=records_student, teacher=records_teacher, segment='class')

        try:
            record_class = StudentClass()
            record_class.code = code
            record_class.class_name = name
            db.session.add(record_class)
            db.session.flush()

            if teacher:
                record_teacher = Teacher.query.filter(
                    Teacher.id == teacher).filter(
                    Teacher.deleted == False).first()

                record_class.teacher = record_teacher.name

            if student:
                records_student = Student.query.filter(
                    Student.id.in_(student)).filter(
                    Student.deleted == False).all()

                for data_student in records_student:
                    record_class.student.append(data_student)

            db.session.commit()

            return redirect('/class')
        except Exception as e:
            print(traceback.format_exc())
            return render_template('student_class/class-info.html', has_error='Error!', student=records_student, teacher=records_teacher, segment='class')


@blueprint.route('/info-class/<id>', methods=['GET', 'POST'])
@login_required
def student_info(id):
    if request.method == 'GET':
        record_class = StudentClass.query.filter(
            StudentClass.id == id).filter(
            StudentClass.deleted == False).first()

        records_student = record_class.student

        records_teacher = Teacher.query.filter(
            Teacher.deleted == False).all()

        return render_template('student_class/class-info.html', student_class=record_class, student=records_student, teacher=records_teacher, segment='class')

    if request.method == 'POST':
        code = request.form.get('code')
        name = (request.form.get('name')).replace(',', " ")
        teacher = request.form.get('teacher')

        records_student = Student.query.filter(
            Student.deleted == False).all()

        records_teacher = Teacher.query.filter(
            Teacher.deleted == False).all()

        if not code:
            return render_template('student_class/class-info.html', has_error='Code is empty!', student=records_student, teacher=records_teacher, segment='class')
        if not name:
            return render_template('student_class/class-info.html', has_error='Name is empty!', student=records_student, teacher=records_teacher, segment='class')
        if not teacher:
            return render_template('student_class/class-info.html', has_error='Teacher is empty!', student=records_student, teacher=records_teacher, segment='class')

        record_class = StudentClass.query.filter(
            StudentClass.id == id).filter(
            StudentClass.code == code).filter(
            StudentClass.deleted == False).first()
        if record_class:
            return render_template('student_class/class-info.html', has_error='Class code already exists!', student=records_student, teacher=records_teacher, segment='class')

        try:
            record_class = StudentClass.query.filter(
                StudentClass.id == id).filter(
                StudentClass.deleted == False).first()

            record_class.code = code
            record_class.class_name = name

            if teacher:
                record_teacher = Teacher.query.filter(
                    Teacher.id == teacher).filter(
                    Teacher.deleted == False).first()

                record_class.teacher = record_teacher.name

            db.session.commit()

            return redirect('/class')
        except Exception as e:
            print(traceback.format_exc())
            return render_template('student_class/class-info.html', has_error='Error!', student=records_student, teacher=records_teacher, segment='class')


@blueprint.route('/class/<id>')
@login_required
def class_delete(id):
    record_class = StudentClass.query.filter(
        StudentClass.id == id).filter(
        StudentClass.deleted == False).first()
    record_class.deleted = True
    db.session.commit()
    return redirect('/class')

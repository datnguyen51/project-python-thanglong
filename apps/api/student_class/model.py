# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from apps import db


def default_uuid():
    return str(uuid.uuid4())


class StudentClass(db.Model):

    __tablename__ = 'student_class'

    id = db.Column(db.String(100), primary_key=True, default=default_uuid)
    code = db.Column(db.String(250))
    class_name = db.Column(db.String(250))
    teacher = db.Column(db.String(250))
    deleted = db.Column(db.Boolean(), default=False)
    student = relationship('Student', secondary='student_of_class', back_populates='class_student')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, property, value)


class StudentOfClass(db.Model):
    __tablename__ = 'student_of_class'

    id = db.Column(db.String(100), primary_key=True, default=default_uuid)
    student_class_id = db.Column(db.String(250), ForeignKey('student_class.id'), primary_key=True)
    student_id = db.Column(db.String(250), ForeignKey('student.id'), primary_key=True)

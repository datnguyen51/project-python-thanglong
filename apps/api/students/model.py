import uuid
from sqlalchemy.orm import relationship

from apps import db
from apps.api.student_class.model import StudentClass, StudentOfClass


def default_uuid():
    return str(uuid.uuid4())


class Student(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.String(100), primary_key=True, default=default_uuid)
    code = db.Column(db.String(64), unique=True)
    avatar = db.Column(db.String(250))
    name = db.Column(db.String(250))
    address = db.Column(db.String(250))
    gender = db.Column(db.String())
    birthday = db.Column(db.DateTime())
    phone_number = db.Column(db.String(100))
    email = db.Column(db.String(100))
    identification = db.Column(db.String(100))  # Căn cước công dân
    health_insurance = db.Column(db.String(100))  # Bảo hiểm y tế
    student_class = db.Column(db.String(100))
    student_major = db.Column(db.String(100))
    deleted = db.Column(db.Boolean(), default=False)
    class_student = relationship(
        'StudentClass', secondary='student_of_class', back_populates='student')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.code)

from app.database.database import SessionLocal
from app.models.student import Student


class StudentService:

    @staticmethod
    def next_admission_number():

        db = SessionLocal()

        try:
            count = db.query(Student).count()
            return f"2026{count + 1:04d}"

        finally:
            db.close()

    @staticmethod
    def add_student(student):

        db = SessionLocal()

        try:
            db.add(student)
            db.commit()

        finally:
            db.close()

    @staticmethod
    def get_students():

        db = SessionLocal()

        try:
            return db.query(Student).all()

        finally:
            db.close()

    @staticmethod
    def delete_student(student_id):

        db = SessionLocal()

        try:
            student = db.query(Student).get(student_id)

            if student:
                db.delete(student)
                db.commit()

        finally:
            db.close()
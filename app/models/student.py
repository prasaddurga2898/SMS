from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    admission_no = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    gender = Column(String(20))
    dob = Column(String(20))
    student_class = Column(String(20))
    section = Column(String(10))
    father_name = Column(String(150))
    mother_name = Column(String(150))
    mobile = Column(String(20))
    address = Column(String(255))
    photo = Column(String(255))
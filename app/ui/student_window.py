from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from app.models.student import Student
from app.services.student_service import StudentService


class StudentWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Management")

        self.resize(450, 450)

        self.admission = QLineEdit()
        self.admission.setReadOnly(True)
        self.admission.setText(StudentService.next_admission_number())

        self.first = QLineEdit()

        self.last = QLineEdit()

        self.mobile = QLineEdit()

        save = QPushButton("Save Student")

        save.clicked.connect(self.save_student)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Admission No"))
        layout.addWidget(self.admission)

        layout.addWidget(QLabel("First Name"))
        layout.addWidget(self.first)

        layout.addWidget(QLabel("Last Name"))
        layout.addWidget(self.last)

        layout.addWidget(QLabel("Mobile"))
        layout.addWidget(self.mobile)

        layout.addWidget(save)

        self.setLayout(layout)

    def save_student(self):

        student = Student(
            admission_no=self.admission.text(),
            first_name=self.first.text(),
            last_name=self.last.text(),
            mobile=self.mobile.text(),
        )

        StudentService.add_student(student)

        QMessageBox.information(
            self,
            "Success",
            "Student Saved Successfully!"
        )

        self.close()
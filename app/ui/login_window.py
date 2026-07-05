from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
from PySide6.QtCore import Qt


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("EduSphere School Management System")
        self.resize(420, 300)

        title = QLabel("EduSphere")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "font-size:24px;font-weight:bold;color:#1E88E5;"
        )

        subtitle = QLabel("School Management System")
        subtitle.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def login(self):

        if (
            self.username.text() == "admin"
            and self.password.text() == "admin123"
        ):
            QMessageBox.information(
                self,
                "Success",
                "Login Successful!"
            )
        else:
            QMessageBox.warning(
                self,
                "Error",
                "Invalid Username or Password"
            )
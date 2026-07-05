from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from app.services.auth_service import AuthService
from app.ui.dashboard import Dashboard


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
        user = AuthService.login(
            self.username.text(),
            self.password.text()
        )

        if user:
            self.dashboard = Dashboard(user)
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Login Failed",
                "Invalid username or password"
            )
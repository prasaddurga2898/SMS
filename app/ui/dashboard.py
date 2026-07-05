from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QFrame,
    QStatusBar,
    QMessageBox,
)


class Dashboard(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("EduSphere School Management System")
        self.resize(1200, 700)

        self.create_ui()

    def create_card(self, title, value):

        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("""
            QFrame{
                border:1px solid #cccccc;
                border-radius:8px;
                background:white;
            }
        """)

        layout = QVBoxLayout(frame)

        title_lbl = QLabel(title)
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setStyleSheet("font-size:16px;")

        value_lbl = QLabel(str(value))
        value_lbl.setAlignment(Qt.AlignCenter)
        value_lbl.setStyleSheet(
            "font-size:28px;font-weight:bold;color:#1565C0;"
        )

        layout.addWidget(title_lbl)
        layout.addWidget(value_lbl)

        return frame

    def create_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # Header
        title = QLabel("EduSphere School Management System")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#1565C0;
            padding:10px;
        """)

        main_layout.addWidget(title)

        # Menu Buttons
        menu = QHBoxLayout()

        buttons = [
            "Dashboard",
            "Students",
            "Teachers",
            "Attendance",
            "Fees",
            "Reports",
            "Settings",
        ]

        for text in buttons:
            btn = QPushButton(text)
            btn.setMinimumHeight(40)
            menu.addWidget(btn)

        logout = QPushButton("Logout")
        logout.clicked.connect(self.logout)
        menu.addWidget(logout)

        main_layout.addLayout(menu)

        # Statistics
        grid = QGridLayout()

        grid.addWidget(self.create_card("Students", 0), 0, 0)
        grid.addWidget(self.create_card("Teachers", 0), 0, 1)
        grid.addWidget(self.create_card("Classes", 0), 0, 2)
        grid.addWidget(self.create_card("Fees", "₹0"), 0, 3)

        main_layout.addLayout(grid)

        # Welcome
        welcome = QLabel(
            f"Welcome {self.user.full_name}\nRole : {self.user.role}"
        )
        welcome.setStyleSheet("font-size:18px;padding:20px;")

        main_layout.addWidget(welcome)

        # Status Bar
        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def logout(self):

        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?"
        )

        if reply == QMessageBox.Yes:
            self.close()
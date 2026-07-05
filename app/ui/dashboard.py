from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGridLayout,
    QListWidget,
    QListWidgetItem,
    QStatusBar,
    QMenuBar,
    QToolBar,
    QMessageBox
)


class Dashboard(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("EduSphere School Management System")
        self.resize(1300, 750)

        self.create_menu()
        self.create_toolbar()
        self.create_ui()

    def create_menu(self):

        menubar = self.menuBar()

        menubar.addMenu("File")
        menubar.addMenu("Students")
        menubar.addMenu("Teachers")
        menubar.addMenu("Attendance")
        menubar.addMenu("Fees")
        menubar.addMenu("Reports")
        menubar.addMenu("Settings")
        menubar.addMenu("Help")

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

    def create_card(self, title, value):

        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("""
            QFrame{
                background:white;
                border:1px solid #cfd8dc;
                border-radius:8px;
            }
        """)

        layout = QVBoxLayout(frame)

        lbl_title = QLabel(title)
        lbl_title.setAlignment(Qt.AlignCenter)
        lbl_title.setStyleSheet("font-size:16px;")

        lbl_value = QLabel(str(value))
        lbl_value.setAlignment(Qt.AlignCenter)
        lbl_value.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#1565C0;
        """)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)

        return frame

    def create_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)

        # ---------------- Left Navigation ----------------

        nav = QListWidget()
        nav.setFixedWidth(220)

        menus = [
            "🏠 Dashboard",
            "👨‍🎓 Students",
            "👩‍🏫 Teachers",
            "📅 Attendance",
            "💰 Fees",
            "📝 Examinations",
            "📚 Library",
            "🚌 Transport",
            "📊 Reports",
            "⚙ Settings"
        ]

        for item in menus:
            nav.addItem(QListWidgetItem(item))

        root.addWidget(nav)

        # ---------------- Right Panel ----------------

        right = QVBoxLayout()

        title = QLabel("EduSphere School Management System")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#1565C0;
            padding:10px;
        """)

        right.addWidget(title)

        welcome = QLabel(
            f"Welcome, {self.user.full_name}\nRole : {self.user.role}"
        )

        welcome.setStyleSheet("""
            font-size:16px;
            padding:15px;
        """)

        right.addWidget(welcome)

        grid = QGridLayout()

        grid.addWidget(self.create_card("Students", 0), 0, 0)
        grid.addWidget(self.create_card("Teachers", 0), 0, 1)
        grid.addWidget(self.create_card("Classes", 0), 0, 2)
        grid.addWidget(self.create_card("Pending Fees", "₹0"), 0, 3)

        right.addLayout(grid)

        info = QLabel("""

Welcome to EduSphere School Management System.

Use the navigation panel on the left to manage:

• Students

• Teachers

• Attendance

• Fees

• Library

• Reports

• Settings

        """)

        info.setStyleSheet("""
            background:white;
            border:1px solid #cccccc;
            padding:15px;
            font-size:14px;
        """)

        right.addWidget(info)

        logout = QPushButton("Logout")
        logout.setFixedWidth(150)
        logout.clicked.connect(self.logout)

        right.addWidget(logout, alignment=Qt.AlignRight)

        root.addLayout(right)

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def logout(self):

        answer = QMessageBox.question(
            self,
            "Logout",
            "Do you want to logout?"
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.close()
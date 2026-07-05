import sys

from PySide6.QtWidgets import QApplication

from app.database.init_db import initialize_database
from app.ui.login_window import LoginWindow


def main():

    initialize_database()

    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
import bcrypt

from app.database.database import SessionLocal
from app.models.user import User


class AuthService:

    @staticmethod
    def login(username, password):

        db = SessionLocal()

        try:

            user = db.query(User).filter(
                User.username == username
            ).first()

            if not user:
                return None

            if bcrypt.checkpw(
                password.encode(),
                user.password.encode()
            ):
                return user

            return None

        finally:
            db.close()
import bcrypt

from app.database.database import Base, SessionLocal, engine
from app.models.user import User
from app.models.student import Student


def initialize_database():
    # Create all tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        admin = db.query(User).filter(User.username == "admin").first()

        if not admin:
            hashed_password = bcrypt.hashpw(
                "admin123".encode(),
                bcrypt.gensalt()
            ).decode()

            admin = User(
                username="admin",
                password=hashed_password,
                full_name="System Administrator",
                role="Administrator"
            )

            db.add(admin)
            db.commit()

    finally:
        db.close()
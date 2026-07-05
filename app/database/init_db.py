import bcrypt

from app.database.database import Base
from app.database.database import SessionLocal
from app.database.database import engine
from app.models.user import User


def initialize_database():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    admin = db.query(User).filter(User.username == "admin").first()

    if not admin:

        hashed = bcrypt.hashpw(
            "admin123".encode(),
            bcrypt.gensalt()
        ).decode()

        admin = User(
            username="admin",
            password=hashed,
            full_name="System Administrator",
            role="Administrator"
        )

        db.add(admin)
        db.commit()

    db.close()
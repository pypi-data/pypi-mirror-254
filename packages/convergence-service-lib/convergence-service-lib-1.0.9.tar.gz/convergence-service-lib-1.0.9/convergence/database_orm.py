from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = None
DB_ENGINE = None
DBSessionLocal = None

EntityBase = declarative_base()


def get_db():
    db = DBSessionLocal()
    try:
        yield db
    finally:
        db.close()

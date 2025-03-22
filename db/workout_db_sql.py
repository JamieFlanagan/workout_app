from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models.entities import Base

DATABASE_URL= "sqlite:///workout_tracker.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

"""if __name__ == "__main__":
    init_db()
    print("DB created")"""
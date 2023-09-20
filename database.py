from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_USER = 'postgres'
DB_PASSWORD = 'Baiken2012'
DB_NAME = 'test'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



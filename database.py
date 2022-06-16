"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(connection_string):
    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

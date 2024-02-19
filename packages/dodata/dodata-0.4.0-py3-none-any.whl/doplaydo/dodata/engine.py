"""Initiates the db session."""
from sqlmodel import Session, create_engine
from . import settings

engine = create_engine(settings.dodata_db_connection_url, echo=settings.debug)


def get_session() -> Session:
    """Get the one and only DB session."""
    with Session(engine) as session:
        return session

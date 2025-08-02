from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from secrets_api import fetch_secrets, define_env

class PorticoDB:

    def __init__(self):
        self.SessionLocal = None
        self.engine = None
        self.db_url = None

    def connect(self):
        define_env()
        secrets = fetch_secrets()
        print(secrets)
        self.db_url = secrets["ss.portico.url"]

        if not self.db_url:
            raise ValueError("Portico DB URL not defined")

        self.engine = create_engine(self.db_url)
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        return self.SessionLocal()

    def close(self):
        self.SessionLocal.remove()
        self.engine.dispose()
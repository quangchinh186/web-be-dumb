import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from model.BaseModel import Base

class SQLAlchemyEngine:
    engine = None

    @classmethod
    def initDB(cls):
        load_dotenv('util/.env')
        host = os.getenv("HOST")
        user = os.getenv("DBUSER")
        password = os.getenv("PASSWORD")
        databaseName = os.getenv("DBNAME")
        port = os.getenv("PORT")
        cls.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{databaseName}", pool_recycle=3600)
        Base.metadata.create_all(cls.engine)
    

SQLAlchemyEngine.initDB()
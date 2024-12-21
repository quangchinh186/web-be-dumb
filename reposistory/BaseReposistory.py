from sqlalchemy.orm import Session
from SQLAlchemyEngine import SQLAlchemyEngine

class Reposistory():
    session = Session(SQLAlchemyEngine.engine)

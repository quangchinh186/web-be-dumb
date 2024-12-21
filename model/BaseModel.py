from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def update(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
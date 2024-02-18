from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

base_model = declarative_base()


class BaseModel(base_model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())


class App(BaseModel):
    __tablename__ = 'app'

    access_token: str = Column(String(500))
    refresh_token: str = Column(String(50))
    iss: str = Column(String(50))
    cmp_id: str = Column(String(50), nullable=True)
    apps_id: str = Column(String(50))


class User(BaseModel):
    __tablename__ = 'user'

    swit_id: str = Column(String(100))
    access_token: str = Column(String(500))
    refresh_token: str = Column(String(50))

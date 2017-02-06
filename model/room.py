from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)

    debts = relationship("debts")
    users = relationship("users")

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from model.association_debt_to_user import association_table

Base = declarative_base()


class Debt(Base):
    __tablename__ = 'debts'
    id = Column(Integer, primary_key=True)
    id_room = Column(Integer, ForeignKey('rooms.id'))
    id_user_from = Column(Integer, ForeignKey("users.id"))
    value = Column(Float)
    date = Column(Date)
    label = Column(String)

    room = relationship('rooms')
    user_from = relationship('users')
    users_to = relationship("users",
                            secondary=association_table)

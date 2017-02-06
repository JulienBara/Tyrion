from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from model.association_debt_to_user import association_table

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    id_room = Column(Integer, ForeignKey('rooms.id'))
    name = Column(String)

    debts_from = relationship('debts')
    users_to = relationship("debts",
                            secondary=association_table)

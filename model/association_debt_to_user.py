from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table(
    'association_debts_to_users', Base.metadata,
    Column('id_user', Integer, ForeignKey('users.id')),
    Column('id_debt', Integer, ForeignKey('right.id'))
)

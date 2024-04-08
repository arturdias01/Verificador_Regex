from configs.base import Base
from sqlalchemy import Column, String, Integer


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email_address = Column(String(50))
    cpf = Column(String(11))

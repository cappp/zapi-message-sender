from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Uuid, Text

Base = declarative_base()


class Contact(Base):
    __tablename__ = "Contacts"

    id = Column(Uuid, primary_key=True)
    name = Column(Text)
    phone = Column(Text)

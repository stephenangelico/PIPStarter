#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://stephen:thinkful@localhost:5432/passport')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

Base.metadata.create_all(engine)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport

session.add(beyonce)
session.commit()

print(beyonce.passport.issue_date)
print(passport.owner.name)
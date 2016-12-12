#!/usr/bin/env python3
# Online auction project - main service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime

engine = create_engine('postgresql://stephen:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
	__tablename__ = "items"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	start_time = Column(DateTime, default=datetime.utcnow)

class Customer(Base):
	__tablename__ = "customers"
	
	uid = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	creation_time = Column(DateTime, default=datetime.utcnow)

class Bid(Base):
	__tablename__ = "bids"
	
	bidid = Column(Integer, primary_key=True)
	price = Column(Float, nullable=False)
	bid_time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

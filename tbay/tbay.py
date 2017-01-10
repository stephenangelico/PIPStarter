#!/usr/bin/env python3
# Online auction project - main service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://stephen:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

user_bids_table = Table('user_bids_association', Base.metadata,
	Column('user_id', Integer, ForeignKey('users.uid')),
	Column('bid_id', Integer, ForeignKey('bids.bidid')),
	Column('item_id', Integer, ForeignKey('items.id'))
)

class Item(Base):
	__tablename__ = "items"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	category = Column(String, nullable=False)
	start_time = Column(DateTime, default=datetime.utcnow)

class User(Base):
	__tablename__ = "users"
	
	uid = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	creation_time = Column(DateTime, default=datetime.utcnow)
	items_auctioned = relationship("Item", backref="user")
	items_bidded = relationship("Item", backref="user")
	bids = relationship("Bid", secondary="user_bids_association", backref="user")

class Bid(Base):
	__tablename__ = "bids"
	
	bidid = Column(Integer, primary_key=True)
	price = Column(Float, nullable=False)
	bid_time = Column(DateTime, default=datetime.utcnow)
	item = relationship("Item", backref="bid")

if __name__ == "__main__":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)


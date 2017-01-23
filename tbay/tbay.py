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

#user_bids_table = Table('user_bids_association', Base.metadata,
#	Column('user_id', Integer, ForeignKey('users.uid')),
#	Column('bid_id', Integer, ForeignKey('bids.bidid')),
#	Column('item_id', Integer, ForeignKey('items.id'))
#)

# Relationships:
# User:Bid = One-to-Many
# Item:Bid = One-to-Many
# User:Item = One-to-Many

class Item(Base):
	__tablename__ = "items"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	category = Column(String, nullable=False)
	start_time = Column(DateTime, default=datetime.utcnow)
	owner_uid = Column(Integer, ForeignKey('users.uid'), nullable=False)
	bids = relationship("Bid", backref="item")
	
class User(Base):
	__tablename__ = "users"
	
	uid = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	creation_time = Column(DateTime, default=datetime.utcnow)
	items_auctioned = relationship("Item", backref="owner")
	bids = relationship("Bid", backref="bidder")

class Bid(Base):
	__tablename__ = "bids"
	
	bidid = Column(Integer, primary_key=True)
	price = Column(Float, nullable=False)
	bid_time = Column(DateTime, default=datetime.utcnow)
	item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
	bidder_uid = Column(Integer, ForeignKey('users.uid'), nullable=False)

def createbid(price, itemname, username):
	#bid1 = Bid(price=20, item_id=1, bidder_uid=2)
	#              ^ amount    ^ Buzz       ^ user stephena
	# Returns the description of all of the basesballs
	#session.query(Item.description).filter(Item.name == "baseball").all()
	#A new bid must be greater than the last one
	try:
		price = float(price)
	except ValueError:
		print("Please enter a valid bid value")
		return None
	#TODO: Check to see if new bid is greater than previous bid. If lesser, reject bid.
	biditem = session.query(Item.id).filter(Item.name == itemname).first()
	if biditem is None:
		print("Invalid item name. Please enter a known item.")
		return None
	biduser = session.query(User.uid).filter(User.username == username).first()
	if biduser is None:
		print("Username invalid. Perhaps you need to log in?")
		return None
	newbid = Bid(price=price, item_id=biditem.id, bidder_uid=biduser.uid)
	session.add(newbid)
	session.commit()
	
def highbid(item_id):
	#Return entire highest bid object

def endauction(itemname):
	#Find all bids that are associated with given item ID
	# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
	#session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()
	#Assuming highbid() does its work, the latest bid should be the successful one.
	solditem = session.query(Item.id,Item.name).filter(Item.name == itemname).first()
	if solditem is None:
		print("Invalid item name. Please enter a known item.")
		return None
	winbid = highbid(solditem.id)
	#TODO: Get winning user
	print("{0} placed the highest bid of {1} on the {2}".format([winuser, bidvalue, solditem.name])

if __name__ == "__main__":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)


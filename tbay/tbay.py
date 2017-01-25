#!/usr/bin/env python3
# Online auction project - main service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

# DB connection info
engine = create_engine('postgresql://stephen:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Table definitions
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
	# User-called function to place bids
	# A new bid must be greater than the last one
	
	# Entry validation
	try:
		price = float(price)
	except ValueError:
		print("Please enter a valid bid value")
		return None
	biditem = session.query(Item.id).filter(Item.name == itemname).first()
	if biditem is None:
		print("Invalid item name. Please enter a known item.")
		return None
	biduser = session.query(User.uid).filter(User.username == username).first()
	if biduser is None:
		print("Username invalid. Perhaps you need to log in?")
		return None
	
	# Check to see if new bid is greater than previous bid. If lesser, reject bid. If None returned, assume 0.
	checkbid = highbid(biditem.id, "reject")
	if checkbid is None:
		checkbid = 0
	if checkbid >= price:
		print("The current highest bid is {0}. Your bid ({1}) must be greater to be accepted.".format(checkbid, price))
		return None
	
	# The actual work
	newbid = Bid(price=price, item_id=biditem.id, bidder_uid=biduser.uid)
	session.add(newbid)
	session.commit()
	
def highbid(item_id, mode):
	# For mode 'reject', return just the value.
	# For mode 'close', return entire highest bid object.
	highbid = session.query(func.max(Bid.price)).filter(Bid.item_id == item_id).first()[0]
	if mode == "reject":
		return highbid
	elif mode == "close":
		winbid = session.query(Bid).filter(Bid.item_id == item_id, Bid.price == highbid).first()
		return winbid
	else:
		# Error handling
		print("{} is not a recognized mode.".format(mode))
		raise NameError
	# Below is overengineered and deprecated, awaiting removal after error handling
	#itembids = []
	#itembids.append(session.query(Bid).filter(Bid.item_id == item_id).all())
	#for bid in itembids:
	#	highbid = 0
	#	if bid.price > highbid:
	#		highbid = bid.price
	#		curbid = bid
	#if highbid == 0:
	#	return None
	#else:
	#	return curbid

def endauction(itemname):
	# First turn item name into an ID to work with
	solditem = session.query(Item.id, Item.name).filter(Item.name == itemname).first()
	if solditem is None:
		print("Invalid item name. Please enter a known item.")
		return None
	# Then get the bid we're looking for
	winbid = highbid(solditem.id, "close")
	if winbid is None:
		print("No bids were placed on the {}.".format(solditem.name))
	# Finally, get the winning user
	winuser = session.query(User.username).filter(User.uid == winbid.bidder_uid).first()[0]
	bidvalue = winbid.price
	print("{0} placed the highest bid of {1} on the {2}.".format(winuser, bidvalue, solditem.name))
	#TODO: Remove item and bids at the end

# Just to clear data for testing; otherwise, just import this script into the interpreter
if __name__ == "__main__":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)


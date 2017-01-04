#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://stephen:thinkful@localhost:5432/pizza')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

pizza_topping_table = Table('pizza_topping_association', Base.metadata,
	Column('pizza_id', Integer, ForeignKey('pizza.id')),
	Column('topping_id', Integer, ForeignKey('topping.id'))
)

class Pizza(Base):
	__tablename__ = 'pizza'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	toppings = relationship("Topping", secondary="pizza_topping_association",
			backref="pizzas")

class Topping(Base):
	__tablename__ = 'topping'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)

if __name__ == "__main__":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

peppers = Topping(name="Peppers")
garlic = Topping(name="Garlic")
chilli = Topping(name="Chilli")

spicy_pepper = Pizza(name="Spicy Pepper")
spicy_pepper.toppings = [peppers, chilli]

vampire_weekend = Pizza(name="Vampire Weekend")
vampire_weekend.toppings = [garlic, chilli]

session.add_all([garlic, peppers, chilli, spicy_pepper, vampire_weekend])
session.commit()

for topping in vampire_weekend.toppings:
    print(topping.name)

for pizza in chilli.pizzas:
    print(pizza.name)

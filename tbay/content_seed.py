#!/usr/bin/env python3
from tbay import *

beyonce = User(username="bknowles", password="uhohuhohuhohohunana")
stephen = User(username="stephena", password="guesswhat")

buzz = Item(name="Buzz Lightyear Action Figure", description="12-inch Buzz Lightyear action toy with wings, lights and sounds")
dresser = Item(name="Oak Standing Dresser", description="Red Oak 3-drawer standing dresser")

session.add(beyonce, stephen, buzz, dresser)
session.commit()

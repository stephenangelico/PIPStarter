#!/usr/bin/env python3
from tbay import *

beyonce = User(username="bknowles", password="uhohuhohuhohohunana")
stephen = User(username="stephena", password="guesswhat")
woody = User(username="sheriffwoody", password="theresasnakeinmyboot")

buzz = Item(name="Buzz Lightyear Action Figure", description="12-inch Buzz Lightyear action toy with wings, lights and sounds", category="Toys", user="bknowles")
dresser = Item(name="Oak Standing Dresser", description="Red Oak 3-drawer standing dresser", category="Furniture", user="stephena")
ball = Item(name="Baseball", description="Well-loved baseball", category="Sporting Equipment", user="sheriffwoody")

session.add_all([beyonce, stephen, woody, buzz, dresser, ball])
session.commit()

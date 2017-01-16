#!/usr/bin/env python3
from tbay import *

beyonce = User(username="bknowles", password="uhohuhohuhohohunana")
stephen = User(username="stephena", password="guesswhat")
woody = User(username="sheriffwoody", password="theresasnakeinmyboot")

session.add_all([beyonce, stephen, woody])
session.commit()

buzz = Item(name="Buzz Lightyear Action Figure", description="12-inch Buzz Lightyear action toy with wings, lights and sounds", category="Toys", owner_uid=beyonce.uid)
dresser = Item(name="Oak Standing Dresser", description="Red Oak 3-drawer standing dresser", category="Furniture", owner_uid=stephen.uid)
ball = Item(name="Baseball", description="Well-loved baseball", category="Sporting Equipment", owner_uid=woody.uid)

session.add_all([buzz, dresser, ball])
session.commit()

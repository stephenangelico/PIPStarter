#!/usr/bin/env python3

import sys
import logging
import argparse
import psycopg2

# Logging config: file and level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connect to Postgres database
logging.debug("Connecting to PostgreSQL...")
try:
	connection = psycopg2.connect(database="snippets")
except psycopg2.OperationalError:
	print("Could not connect to snippets database.\nIs the PostgreSQL server running?")
	logging.error("Database connection failed: Operational Error")
	sys.exit(1)
logging.debug("Database connection established.")

def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
	
	subparsers = parser.add_subparsers(dest="command", help="Available commands")
	
	# Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="Name of the snippet")
	put_parser.add_argument("snippet", help="Snippet text")
	
	# Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get", help="Return a stored snippet")
	get_parser.add_argument("name", help="Name of the snippet")
	
	# Subparser for the catalog command
	logging.debug("Constructing catalog subparser")
	catalog_parser = subparsers.add_parser("catalog", help="List stored snippets")
	
	arguments = parser.parse_args()
	# Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	
	if command == "put":
		name, snippet = put(**arguments)
		print("Stored {!r} as {!r}".format(snippet, name))
	elif command == "get":
		try:
			snippet = get(**arguments)
			print("Retrieved snippet: {!r}".format(snippet))
		except NameError:
			print(arguments["name"] + ": 404 Not Found")
			logging.debug("Snippet {} not found".format(arguments["name"]))
	elif command == "catalog":
		
def put(name, snippet):
	"""
	Store a snippet with an associated name.
	
	Returns the name and the snippet
	"""
	#logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
	logging.info("Storing snippet {!r}, {!r}".format(name, snippet))
	with connection, connection.cursor() as cursor:
		try:
			command = "insert into snippets values (%s, %s)"
			cursor.execute(command, (name, snippet))
		except psycopg2.IntegrityError as e:
			connection.rollback()
			command="update snippets set message=%s where keyword=%s"
			cursor.execute(command, (snippet, name))
			logging.warning("Updating {!r} as {!r}.".format(name, snippet))
	logging.debug("Snippet {} stored successfully.".format(name))
	return name, snippet
def get(name):
	"""Retrieve the snippet with the given name.
	
	If there is no such snippet, return '404 Not Found'.
	
	Returns the snippet.
	"""
	#logging.error("FIXME: Unimplemented - get({!r})".format(name))
	logging.info("Retrieving snippet {!r}".format(name))
	with connection, connection.cursor() as cursor:
		cursor.execute("select message from snippets where keyword=%s", (name,))
		row = cursor.fetchone()
	if not row:
		# No snippet found with that name.
		raise NameError(name)
	else:
		return row[0]

if __name__ == "__main__":
	main()

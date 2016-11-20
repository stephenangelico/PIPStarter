#!/usr/bin/env python3

import logging
import argparse
import psycopg2

# Logging config: file and level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connect to Postgres database
logging.debug("Connecting to PostgreSQL...")
connection = psycopg2.connect(database="snippets")
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
	
	arguments = parser.parse_args()
	# Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	
	if command == "put":
		name, snippet = put(**arguments)
		print("Stored {!r} as {!r}".format(snippet, name))
	elif command == "get":
		snippet = get(**arguments)
		print("Retrieved snippet: {!r}".format(snippet))
def put(name, snippet):
	"""
	Store a snippet with an associated name.
	
	Returns the name and the snippet
	"""
	#logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
	logging.info("Storing snippet {!r}, {!r}".format(name, snippet))
	cursor = connection.cursor()
	command = "insert into snippets values (%s, %s)"
	cursor.execute(command, (name, snippet))
	connection.commit()
	logging.debug("Snippet {} stored successfully.".format(name))
	return name, snippet
def get(name):
	"""Retrieve the snippet with the given name.
	
	If there is no such snippet, return '404 Not Found'.
	
	Returns the snippet.
	"""
	#logging.error("FIXME: Unimplemented - get({!r})".format(name))
	logging.info("Retrieving snippet {!r}".format(name))
	cursor = connection.cursor()
	command = "select message from snippets where keyword=%s"
	cursor.execute(command, (name,))
	return cursor.fetchone()

if __name__ == "__main__":
	main()

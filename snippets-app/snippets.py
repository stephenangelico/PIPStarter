import logging
import argparse

# Logging config: file and level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
	arguments = parser.parse_args()
def put(name, snippet):
	"""
	Store a snippet with an associated name.
	
	Returns the name and the snippet
	"""
	logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
	return name, snippet
def get(name):
	"""Retrieve the snippet with the given name.
	
	If there is no such snippet, return '404 Not Found'.
	
	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return ""

if __name__ == "__main__":
	main()
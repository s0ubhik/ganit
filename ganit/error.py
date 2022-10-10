from .token import *

def runtime_error(msg):
	print("Runtime Error: "+msg)

def parser_error(msg, node):
	nd = node
	while nd.pos == ():
		if type(nd.value) in (Token, Node): nd = nd.value

	l,c = nd.pos
	print("ParserError "+str(l)+":"+str(c)+": "+msg)
	exit()

def warning(msg, node):
	nd = node
	while nd.pos == ():
		if type(nd.value) in (Token, Node): nd = nd.value

	l,c = nd.pos
	print("Warning "+str(l)+":"+str(c)+": "+msg)
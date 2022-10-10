env = {}
origin = None

from .stream import *
from .error import *
from .lexer import *
from .parser import *

def operation(node):
	a = walk(node.value[0])
	op = node.value[1]
	b = walk(node.value[2])
	if op.type == 'plus': return a + b
	elif op.type == 'minus': return a - b
	elif op.type == 'div': return a / b
	elif op.type == 'mul': return a * b

def walk(node):
	if node.type == 'statement': walk(node.value)
	elif node.type == 'value': return walk(node.value)
	elif node.type == 'iden':
		if node.value not in env:
			runtime_error("Variable '"+node.value+"' not defined")
			return None
		return env[node.value]
	elif node.type == 'int': return int(node.value)
	elif node.type == 'operation': return operation(node)

	elif node.type == 'assign':
		a = node.value[0].value.value
		b = walk(node.value[1])
		env[a] = b

	elif node.type == 'output':
		a = node.value.value
		out = walk(a)
		print(out)

def run(text):
	global env
	buf_strm = Stream(text)
	tokens = list(lex(buf_strm))

	tkn_strm = TokenStream(tokens)
	nodes = parse(tkn_strm)

	for node in nodes:
		walk(node)
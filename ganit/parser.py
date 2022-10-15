from .token import *
from .error import *

def parse(tkn_strm):
	root = Node('prog', [])

	while tkn_strm.next():
		t = tkn_strm.cur()
		if t.type in ['iden', 'int']:
			tkn_strm.insert(Node('value', t))
			tkn_strm.pop(1)

	tkn_strm.reset()

	while tkn_strm.next():
		t = tkn_strm.cur()
		if t.type in ('mul', 'div'):
			if tkn_strm.backward().type in ('value', 'operation') and tkn_strm.advance().type in ('value', 'operation'):
				a = tkn_strm.pop(-1)
				tkn_strm.pop(-1)
				b = tkn_strm.pop(-1)
				tkn_strm.insert(Node('operation', [a, t, b]), -1)

	tkn_strm.reset()

	while tkn_strm.next():
		t = tkn_strm.cur()
		if t.type in ('plus', 'minus'):
			if tkn_strm.backward().type in ('value', 'operation') and tkn_strm.advance().type in ('value', 'operation'):
				a = tkn_strm.pop(-1)
				tkn_strm.pop(-1)
				b = tkn_strm.pop(-1)
				tkn_strm.insert(Node('operation', [a, t, b]), -1)

	tkn_strm.reset()

	while tkn_strm.next():
		t = tkn_strm.cur()
		if t.type in ['iden', 'int', 'operation']:
			tkn_strm.insert(Node('value', t))
			tkn_strm.pop(1)

	tkn_strm.reset()

	
	while tkn_strm.next():
		t = tkn_strm.cur()

		if t.type == 'value' and tkn_strm.advance().type == 'equ' and tkn_strm.advance(2).type == 'value':
				a = tkn_strm.pop()
				tkn_strm.pop()
				b = tkn_strm.pop()
				tkn_strm.insert(Node('assign', [a, b]))

		if t.type == 'gt' and tkn_strm.advance().type == 'value':
			tkn_strm.pop()
			a = tkn_strm.pop()
			tkn_strm.insert(Node('output', a))

	tkn_strm.reset()

	while tkn_strm.next():
		t = tkn_strm.cur()

		if t.type in ('assign', 'output') and tkn_strm.advance().type == 'semicol':
			cmd = tkn_strm.pop()
			tkn_strm.pop()
			tkn_strm.insert(Node('statement', cmd))

	tkn_strm.reset()

	return tkn_strm.code

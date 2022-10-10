from .token import *
from .error import *

special_chars = {
	"+": "plus",
	"-": "minus",
	"*": "mul",
	"/": "div",
	"=": "equ",
	";": "semicol",
	">": "gt"
}

def collect_iden(buf_strm):
	iden = buf_strm.cur()
	while buf_strm.next():
		c = buf_strm.cur()
		if c.isalnum() or c == "_": iden += c
		else:
			buf_strm.back()
			break
	
	return iden

def collect_int(buf_strm):
	_int = buf_strm.cur()
	while buf_strm.next():
		c = buf_strm.cur()
		if c.isdigit(): _int += c
		else:
			buf_strm.back()
			break
	
	return _int

def lex(buf_strm):
	while buf_strm.next():
		c = buf_strm.cur()
		pos = buf_strm.get_pos()

		# white space
		if c.isspace(): continue

		# identifier
		elif c.isalpha() or c == "_":
			iden = collect_iden(buf_strm)
			yield Token('iden', iden, pos)

		# integers
		elif c.isdigit():
			_int = collect_int(buf_strm)
			yield Token('int', _int, pos)

		# special chars
		elif c in special_chars.keys():
			yield Token(special_chars[c], '', pos)

		else:
			warning("Ignored Illegal Charecter '"+c+"'", Token('', '', pos))
			pass
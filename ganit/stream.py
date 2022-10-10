from .error import *

class Stream:
	def __init__(self, code):
		self.code = code
		self.i = -1
		self.max = len(self.code)

	def next(self):
		if self.max -1 <= self.i : return False
		self.i += 1
		return True

	def back(self):
		if self.i <= 0: return False
		self.i -= 1
		return True

	def cur(self, man = 0):
		return self.code[self.i+man]

	def get_pos(self):
		l = 1
		c = 1
		for i in range(0, self.i):
			if self.code[i] == '\n':
				l += 1
				c = 1
			else: c += 1
		return (l,c)

class TokenStream(Stream):
	def pop(self, man = 0):
		self.max -= 1
		return self.code.pop(self.i+man)

	def insert(self, item, man = 0):
		self.max += 1
		return self.code.insert(self.i + man, item)

	def advance(self, man = 1):
		if self.max -1 <= self.i : parser_error("Expected semi-colon ';' before ending", self.cur())
		return self.code[self.i + man]

	def backward(self, man = 1):
		if self.i <= 0: return False
		return self.code[self.i + man]

	def reset(self):
		self.i = -1
		self.max = len(self.code)
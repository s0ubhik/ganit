class Token:
	def __init__(self, _type, value=None, pos=()):
		self.type = _type
		self.pos = pos
		self.value = value

class Node(Token):
	pass

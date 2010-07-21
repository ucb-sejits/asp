
from codepy.cgen import *

# class to convert from python AST to C++ AST




# classes to express everything in C++ AST

class Expression(Generable):
	def __str__(self):
		raise NotImplementedError

	def generate(self):
		yield str(self) + ';'

class BinOp(Expression):
	def __init__(self, left, op, right):
		self.left = left
		self.op = op
		self.right = right

	def __str__(self):
		return "(%s %s %s)" % (self.left, self.op, self.right)

class UnaryOp(Expression):
	def __init__(self, op, operand):
		self.op = op
		self.operand = operand

	def __str__(self):
		return "(%s(%s))" % (self.op, self.operand)

class Subscript(Expression):
	def __init__(self, value, index):
		self.value = value
		self.index = index

	def __str__(self):
		return "%s[%s]" % (self.value, self.index)

class Call(Expression):
	def __init__(self, func, args):
		self.func = func
		self.args = args

	def __str__(self):
		return "%s(%s)" % (self.func, ", ".join(map(str, self.args)))

# expression types not used in this example:

class PostfixUnaryOp(Expression):
	def __init__(self, operand, op):
		self.operand = operand
		self.op = op

	def __str__(self):
		return "((%s)%s)" % (self.operand, self.op)

class ConditionalExpr(Expression):
	def __init__(self, test, body, orelse):
		self.test = test
		self.body = body
		self.orelse = orelse

	def __str__(self):
		return "(%s ? %s : %s)" % (self.test, self.body, self.orelse)

class TypeCast(Expression):
	# "type" should be a declaration with an empty variable name
	# e.g. TypeCast(Pointer(Value('int', '')), ...)

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return "((%s)%s)" % (self.type.inline(), self.value)

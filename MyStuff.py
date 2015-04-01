class MyStuff(object):

	def __init__(self):
		self.tangerine = "An example"

	def apple(self):
		print "Another example 2"

	@property
	def foo(self):
		return self.tangerine

	def bar(self,value):
		return self.tangerine + value
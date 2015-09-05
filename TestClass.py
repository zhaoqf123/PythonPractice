class MyClass:
	'''It is really amazing!'''
	i = 12345
	def func(self, x):
		return "The twice of x is:", 2*x

	def func2(self):
		return self.y*3

class P(object):
	def __init__(self,x):
		self.x = x

	def pop(self, value):
		return 3*value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self,x):
		if x < 0:
			self.__x = 0
		elif x > 1000:
			self.__x = 1000
		else:
			self.__x = x
	'''
    def pop(self,value):
    	pass
   		return self.x + value
   	'''
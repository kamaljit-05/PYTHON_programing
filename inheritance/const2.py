class A:
	def __init__ (self):
		self.x=10
	def displayA(self):
		print(self.x)
class B(A):
	def __init__(self):
		super().__init__()
		self.y=20
	def displayB(self):
		print(self.y)
ob=B()
ob.displayA()
ob.displayB()
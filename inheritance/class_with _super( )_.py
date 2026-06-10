#Example 3: Derived class with super() to call parent constructor
class A:
	def __init__(self):
		print("A construtor")
class B(A):
	def __init__(self ):
		print("B constructor")
ob=B()


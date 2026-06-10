class A:
	def __init__(self):
		print("A construtor")
class B(A):
	def __init__(self,x):
		super().__init__()
		print("B constructor",x)
ob=B(10)

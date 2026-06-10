class A:
	def __init__(self,x):
		print("A constructer",x)
class B(A):
	def __init__(self,x,y=0):
		super().__init__(x)
		print("B constructor",y)

ob=B(10)
obj=B(30,40)
class A:
	def show(self):
		print("A show")
class B(A):
	def show(self):
		super().show()
		print("B show")
ob=B()
ob.show()

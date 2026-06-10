 #Example 4: Passing Arguments to Base Constructor
class parent:
	def __init__(self,name):
		print("parent constructer: ",name)
class child(parent):
	def __init__(self,name,age):
		super().__init__(name) #passing argumennt to base
		print ("child constructor: ",age)
obj=child("jhon",23)


'''
Case	                         Behavior
No constructor 				in child	Parent constructor is called automatically
constructors				 in child, no super()	Parent constructor is not called
Constructor 				in child with super()	Both constructors are called
Constructor with arguments				Use super().__init__(args) to pass    '''
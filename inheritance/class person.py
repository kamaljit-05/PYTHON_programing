class person:
	def __init__(self,name,age):
		self._name=name
		self._age=age
	def set__name(self,name):
		self._name=name
	def set__age(self,age):
		self._age=age
	def get__name(self):
		print(self._name)
	def get__age(self):
		print(self._age)
class employee(person):
	def __init__(self,name,age,Id,salary,mob):
		super().__init__(name,age)
		self._Id=Id
		self._salary=salary
		self._mob=mob
	def set__Id(self,Id):
		self._Id=Id
	def set__salary(self,salary):
		self._salary=salary
	def set__mob(self,mob):
		self._mob=mob
	def get__Id(self):
		print(self._Id)
	def get__salary(self):
		print(self._salary)
	def get__mob(self):
		print(self._mob)
obj=person("ram",23)
obj.get__name()
obj.get__age()
obj.set__name("sam")
obj.set__age(24)
obj.get__name()
obj.get__age()


obj1=employee("gopal",25,"ME202",70000,1425678901)
obj1.get__name()
obj1.get__age()
obj1.get__Id()
obj1.get__salary()
obj1.get__mob()
obj1.set__name("sam")
obj1.set__age(24)
obj1.set__Id("ME102")
obj1.set__salary(80000)
obj1.set__mob(1425677601)

obj1.get__name()
obj1.get__age()
obj1.get__Id()
obj1.get__salary()
obj1.get__mob()
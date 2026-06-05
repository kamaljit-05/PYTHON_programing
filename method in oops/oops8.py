class Student:
    name="#"   #class variable   common for all object
    rollno=0   # class variable 
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 
print(s.__dict__)  # { }
print(Student.__dict__)

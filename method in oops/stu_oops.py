class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(s):  #self postion write any name
        print("my name=",s.name)
        print("my rollno=",s.rollno)
print("enter student name and rollno")
nam=input()
rol=int(input())
s=Student(nam,rol)
s.show()


class Rectangle:
    def __init__(self,L,B):  
        self.L=L
        self.B=B
    def show(self):  
        print("length=",self.L)
        print("breadth=",self.B)
    def area(self):
        return self.L*self.B 
    def peri(self):
        print("perimeter=",2*(self.L+self.B))
print("enter rectangle length and breadth ")
Len=float(input())
Bre=float(input())
r=Rectangle(Len,Bre)
r.show()
print("area of rectangle=",r.area())
r.peri()

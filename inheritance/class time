class time:
	def __init__(self,d,h,m,s):
		self.d=d
		self.h=h
		self.m=m
		self.s=s
	def show(self):
		print("the time is ",self.d,"days",self.h,"hour",self.m,"min",self.s,"sec")
	def __add__(self,t2):
		t3=time(0,0,0,0)
		t3.s=self.s+t2.s
		if t3.s>=60:
			t3.m=t3.m+t3.s//60
			t3.s=t3.s%60
		t3.m+=self.m+t2.m
		if t3.m>=60:
			t3.h+=t3.m//60
			t3.m=t3.m%60
		t3.h+=self.h+t2.h
		if t3.h>=24:
			t3.d+=t3.h//24
			t3.h=t3.h%24
		t3.d+=self.d+t2.d
		return t3


t1=time(1,2,3,30)
t1.show()
t2=time(2,8,5,35)
t2.show()
t3=t1+t2
t3.show()
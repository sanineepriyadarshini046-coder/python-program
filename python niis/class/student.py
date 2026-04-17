class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("my name=",self.name)
		print("my roll no=",self.roll)
		print("my mark=",self.mark)
s1=student("saninee",1,90.00)
s2=student("san",2,94.99)
s1.show()
s2.show()
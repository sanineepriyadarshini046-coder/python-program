class sical:
	def __init__(self,p,t,r):
		self.princpal=p
		self.time=t
		self.rate=r
	def show(self):
		print("princpal=",self. princpal)
		print("time=",self.time)
		print("rate=",self.rate)
	def calculate(self):
		return self.princpal*self.rate*self.time/100
s1=sical(1000,10,2)
s1.show()
print("simple interest=",s1.calculate())

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
print("enter princpal rate and time")
#s1=calculate(float(input()),float(input()),float(input()))
pr=float(input())
r=float(input())
t=float(input())
s1=sical(pr,t,r)
s1.show()
print("simple interest=",s1.calculate())

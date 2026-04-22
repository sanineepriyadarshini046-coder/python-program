class rectangle:
	def __init__(self,length,breath):
		self.length = length
		self.breath = breath
	def area(self):
		result = self.length*self.breath
		print("Area of rectangle:",result)
l = int(input("Enter length: "))
b = int(input("Enter breath: "))

r1 = rectangle(l,b)

r1.area()

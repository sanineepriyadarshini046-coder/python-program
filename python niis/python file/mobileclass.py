class Mobile:
	def __init__(self,brand,price):
		self.brand = brand
		self.price = price
	def display(self):
		print("mobile brand:",self.brand)
		print("mobile price:",self.price)
	def budget(self):
		if self.price > 20000:
			print("Expensive")
		else:
			print("Budget phone")
b1 = Mobile("vivo",40000)
b1.display()
b1.budget()
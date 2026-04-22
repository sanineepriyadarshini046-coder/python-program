class CAR:
	def __init__(self,brand,price):
		self.brand=brand
		self.price=price
	def display(self):
		print("CAR brand is:",self.brand)
		print("CAR price is:",self.price)
C1=CAR("SUZUKI",200000)
C2=CAR("SCORPIO",300000)
C1.display()
C2.display()
class dog:
	def __init__(self,name,breed,color):
		self.name = name
		self.breed = breed
		self.color = color

	def bark(self):
		print("dog is barking",self.name)
	def eat(self):
		print("dog eating food",self.breed)
d1 = dog("tommy","golden retriver","white")
d1.eat()
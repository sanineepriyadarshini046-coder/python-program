class book:
	def __init__(self,title,price):
		self.title = title
		self.price = price
	def display(self):
		print("book title:",self.title)
		print("book price:",self.price)
#print("enter title of book:")
#t = input()
#print("enter price:")
#p = int(input())

b1 = book("physics",1000) # b1 = book(t,p)
b1.display()
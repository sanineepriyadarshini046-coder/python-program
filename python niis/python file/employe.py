class employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def display(self):
		print("Employee name:",self.name)
		print("salary",self.salary)
	def bonus(self):
		if self.salary>50000:
			print("Bonus:5000")
		else:
			print("Bonus:2000")
print("enter name of the employee:")
n=str(input())
print("enter salary:")
s=int(input())

e1=employee(n,s)
e1.display()
e1.bonus()
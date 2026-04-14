#prime no
def prime(no):
	if no<=1:
		print("not prime")
	else:
		for i in range(2,no):
			if no%i==0:
				print("not prime")
				break
			else:
				print("prime")
print("enter a no")
no=int(input())
prime(no)


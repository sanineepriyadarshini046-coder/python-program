print("Enter the three number:")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1>=n2:
	if n1>=n3:
		print("number 1 is greater",n1)
	else:
		print("third number is greater",n3)
else:
	if n2>=n3:
		print("second is bigger",n2)
	else:
		print("third mumber is greater",n3)
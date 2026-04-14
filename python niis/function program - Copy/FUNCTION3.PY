#LARGEST OF 3 NO.
def large(no1,no2,no3):
	if no1>=no2:
		if no1>=no3:
			print("no1 is greater")
		else:
			print("no3 is greater")
	else:
		if no2>=no3:
			print("no2 is greater")
		else:
			print("no3 is greater")
print("no1=")
no1=int(input())
print("no2=")
no2=int(input())
print("no3=")
no3=int(input())
large(no1,no2,no3)




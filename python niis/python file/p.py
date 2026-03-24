print("enter 3 number:")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("no1 is greatest")
	else:
		print("no3 is greatest")
else:
	if no2>=no3:
		print("no2 is greatest")
	else:
		print("no3 is greatest")

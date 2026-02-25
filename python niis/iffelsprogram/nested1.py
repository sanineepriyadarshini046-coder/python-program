#wap take 3 number from keybord display biggest no.
print("enter three no")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first no is biggest",no1)
	else:
		print("third no is biggest",no3)
else:
	if no2>=no3:
		print("second no is biggest",no2)
	else:
		print("third no is biggest",no3)
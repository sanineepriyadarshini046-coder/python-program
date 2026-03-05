def add ():
	print ("enter a number")
	no1=int(input())
	print("enter another number ")   #return value with no argument.
	no2=int(input())
	s=no1+no2
	print("sum=",s)
	return
res=add()
print("sum=",res)

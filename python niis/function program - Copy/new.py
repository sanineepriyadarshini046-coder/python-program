def sicl():
	print("enter the principle:")
	p=float(input())
	print("enter the rate:")
	r=float(input())
	print("enter the time:")
	t=float(input())
	si=p*t*r/100
	return si
res=sicl()
print("simple intrest=",res)

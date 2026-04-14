#factorial
def fac(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	print("factorial no=",f)
print("enter a no:")
no=int(input())
fac(no)

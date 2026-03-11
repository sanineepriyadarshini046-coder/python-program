def sical(p,t,r):
	si=p*t*r/100
	return si
res=sical(2,3,4)
print(res)

#in lambda
res=lambda p,t,r:p*t*r/100
print(res(2,3,4))

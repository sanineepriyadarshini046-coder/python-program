"""wap take emp salary from keybord if sal>=5000 da=30% hra=20% 
then display basic salary da hra and total sal"""
print("enter basic salary")
sal=int(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsal=sal+da+hra
print("salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)

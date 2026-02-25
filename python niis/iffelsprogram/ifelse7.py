"""wap take emp salary from keybord if sal>=5000 da=30% hra=20% 
then display basic salary da hra and total sal"""
print("enter basic salary")
sal=float(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)

#wap take a number from keybord chek no is sd dd td od +ve no chek
print("enter a number")
no=int(input())
if no<0:
   no=-no
if no<10:
   print("sd")
elif no<100:
   print("dd")
elif no<1000:
   print("td")
else:
   print("od")
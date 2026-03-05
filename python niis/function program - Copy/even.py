def check():
    print("enter a number")
    no=int(input())
    if no%2==0:
       return True
    else:
       return False
if check():
    print("even number") #return value with argument.
else:
    print("odd number")
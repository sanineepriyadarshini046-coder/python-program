#local&global variabl.
a=10#global
def show():
	a=30#local
	print(a) #local 30
	print(locals()['a'])#local 30
	print(globals()['a'])#global 10
	globals()['a']=40
show()
print(a)
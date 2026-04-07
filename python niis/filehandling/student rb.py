import pickle
from student import student

f=open("student.dat","rb")
print("student recrord:")
while True:
	try:
		s=pickle.load(f)
		s.show()
	except EOFError:
		break

f.close()

import pickle
from student import student


f=open("student.dat","wb")
s1=student(101,"Amit",85)
s2=student(102,"Ravi",90)
s3=student(103,"sita",88)

pickle.dump(s1,f)
pickle.dump(s2,f)
pickle.dump(s3,f)
f.close()
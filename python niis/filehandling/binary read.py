import pickle
f=open("xyz.dat","rb")
print(pickle.load(f))
f.close()
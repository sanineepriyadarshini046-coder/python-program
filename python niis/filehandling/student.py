import pickle

class student:
    def __init__(self, roll, name, mark):
	    self.roll=roll
	    self.name=name
	    self.mark=mark


    def show(self):
       print(self.roll, self.name, self.mark)
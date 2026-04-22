class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def average(self):
        avg = self.total() / 3
        return avg

    def result(self):
        avg = self.average()
        if avg >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

    def display(self):
        print("Name:", self.name)
        print("Total Marks:", self.total())
        print("Average:", self.average())


# Taking input
name = input("Enter name: ")
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

# Creating object
s1 = Student(name, m1, m2, m3)

# Calling methods
s1.display()
s1.result()
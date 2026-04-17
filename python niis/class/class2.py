class student:
    def _init_(self, n, r, m):
        self.name = n
        self.roll = r
        self.mark = m

    def show(self):
        return self

# object creation
s1 = student("san", 1, 90.00)

res = s1.show()

print(type(res), res)
print("my name=", res.name)
print("my roll=", res.roll)
print("my mark=", res.mark) 
import re
txt = "the rain in spain"
x = re.findall("[^a-d]",txt)
print(x)
import re
pattern = re.compile(r'\d+')

result = pattern.findall('abc123ab56c')
print(result)
import re

result = re.match(r'\d+','123ab56c')
print(result.group())
#re.match()-check for a match only at the beging of the string
import re
s = 'hello hi i am ajay 1234 and 56789'
p = input("enter the string: ")
result = re.findall(p,s)
print(result)
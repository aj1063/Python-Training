import random
n = int(input("Enter a number: "))
l = []
i = 0
while i<n:
    l.append(random.randint(1,100))
    i = i+1
print(l) 
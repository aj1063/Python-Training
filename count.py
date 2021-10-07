n=input("enter the string:")
k=n.split()
l=[]
for i in k:
	if (k.count(i)>=1):
		if i not in l:
			l.append(i)
print(' '.join(l))
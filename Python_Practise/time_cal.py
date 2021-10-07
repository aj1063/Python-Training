import sys
import random
import time

if len(sys.argv)!=2:
    print('I need one in put from CLI: ')
    sys.exit(1)

n = int(sys.argv[1])
L = [[0 for i in range(n)] for j in range(n)]
total = n * n
start = time.time()
i = 0
while i<total:
    r1 = random.randint(0,n-1)
    c1 = random.randint(0,n-1)
    data = random.randint(1,1000)
    if L[r1][c1]==0: 
        L[r1][c1]=data
        i = i + 1
end = time.time()
print("Total time is = ",end-start)
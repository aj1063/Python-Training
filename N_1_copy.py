#content of N-1 file copy into Nth file using CLI inteface
import sys
if len(sys.argv)<3:
	print("Please give min 2 file: ")
	sys.exit(1)
n = len(sys.argv)-1
fout = open(sys.argv[-1],'w')	
i = 1
while i<n:
	f = open(sys.argv[i],'r')
	#line = readlines(f)
	while True:
		line = f.readlines()
		if len(line)==0:break
		fout.writelines(line)
	f.close()
	print()
	i = i+1
		
	
fout.close()	
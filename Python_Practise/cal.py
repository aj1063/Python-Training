class Calsi:
	def __init__(self,x,y):
		self.first=x
		self.second=y
	def __str__(self):
		return "Calsi({0},{1})".format(self.first,self.second)	
	def add(self):
		return self.first+self.second
	def sub(self):
		return self.first-self.second
	def mult(self):
		return self.first*self.second
	def div(self):
		return self.first/self.second
		
x = int(input("Enter first data: "))
y = int(input("Enter second data: "))
obj = Calsi(x,y)
print(obj)
#Services = {1:obj.add(),2:obj.sub(),3:obj.mult(),4:obj.div()}

#obj = Calsi(x,y)
while True:
	Services = {1:obj.add(),2:obj.sub(),3:obj.mult(),4:obj.div()}
	print("\t1Menu\n")
	print("1.addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Exit")
	ch = int(input("Enter Your choice: "))
	if ch==5: break
	if ch<1 and ch>4:
		print("Enter right choice: ")
		continue
	#x = int(input("Enter first data: "))
	#y = int(input("Enter second data: "))5
	#if ch==1:
	#	print("Result is ",obj.add())		
	result = Services[ch]
	print("Result is = ",result)
	
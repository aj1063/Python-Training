
print('Hello How are You: ')
l = [10,12,134]

try:	

	x = int(input('Enter first number: '))
	y = int(input('Enter the second number: '))
	z = x / y
	print('z = ',z)
	print(l[1])
except ValueError:
	print("I got a ValueError")
except IndexError:
	print('I got a IndexError')
except ZeroDivisionError:
	print('I got a ZeroDivisionErro')
except Exception:
	print('I got some other error')
	exit(0)
else:
	print('No Exception handling')
finally:
	print('Rest of the app goes here')
			

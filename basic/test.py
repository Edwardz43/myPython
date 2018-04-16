#!D:\python3.6.5\python
#user_input = str(input('username : '))
#print(user_input)
sum = 0
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		print(n, 'is a prime number')
		sum += 1
print(sum)


for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)
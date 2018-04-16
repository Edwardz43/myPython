def fib(n):
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print('end')

print(fib.__doc__)
fib(2000)


def fib2(n):
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
print(fib2.__doc__)
f100 = fib2(100)
print(f100)
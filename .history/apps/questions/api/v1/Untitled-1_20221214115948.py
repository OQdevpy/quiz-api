def Fibonacci(n):
	if n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

def tub(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=[Fibonacci(i) for i in range(1,21)]
b=[i for i in range(1,72) if tub(i)]
print(b)
print(a)



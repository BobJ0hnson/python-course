### generator
num = int(input('Input number: '))

def Fibonacci(n):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
fib_list = list(Fibonacci(num))
print(fib_list[num-1])


### generator
num = int(input('Input number: '))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
fib_list = list(fibonacci(num))
print(fib_list[num-1])


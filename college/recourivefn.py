x=int(input("Enter a number: "))
def rec(n):
    if n == 0:
        return 1
    else:
        return n * rec(n - 1) 

print(rec(x))

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(sum(x))

def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(x))
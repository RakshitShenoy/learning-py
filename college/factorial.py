x=int(input("enter number for factorial"))
factorial=0
def fac(x):
    factorial=0
    for y in range (1,x+1):
        factorial*=y
    return factorial

print(fac(x))

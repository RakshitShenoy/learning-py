def input_numbers():
    n = int(input("Enter the number of times to greet: "))
    c = int(input("Enter the first number: "))
    d = int(input("Enter the second number: "))
    return n, c, d
n, c, d = input_numbers()

def greet(name):
    print(f"Hello, {name}!")

x=0
while x<n:
    greet("Rakshit")
    x+=1

def add(a, b):
    return a + b 
print(add(c, d)) 

def pow(num,exp=2):
    return num ** exp

print(pow(c))
print(pow(d,3))

def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))

def mix(name,*numb,**key):
    print(f"Name: {name}")
    print("Numbers:", numb)
    print("Keyword:", key)

print(mix("Rakshit", 1, 2, 3, age=18, city="mumbai"))    

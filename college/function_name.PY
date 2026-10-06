name=str(input("Enter your name: "))
n=int(input("Enter the number of times u want to be greeted: "))
def printname(name):
    print(f"Hello, {name}!")
x=0
while x<n:
    printname(name)
    x+=1

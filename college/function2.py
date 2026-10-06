from function3 import add_all2
n=[]
for i in range (5):
    n.append(int(input("Enter a number: ")))
def odd_even(n):
   for i in range(len(n)):
       if n[i] % 2 == 0:
           print(f"{n[i]} is even")
       else:
           print(f"{n[i]} is odd")

  
odd_even(n)
print(add_all2(*n))

    
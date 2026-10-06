row=int(input("Enter the number of rows: "))

for i in range(0,row,2):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(i+1):    
        print("* ",end="")
    print()

row=row-2 

for i in range(row-1,-2,-2):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i+1):    
        print(" *",end="")
    print()
row=int(input("Enter the number of rows: "))

if(row %2==0):
    print("Please enter odd number of rows")
else:
    row=int((row+1)/2)
    for i in range(row):
        for j in range(row-i-1):
            print(" ",end="")
        for k in range(2*i+1):    
            print("*",end="")
        print() 

    row=row-1
    for i in range(row):
        for j in range(i+1):
            print(" ",end="")
        for k in range(2*(row-i)-1):    
            print("*",end="")
        print()       
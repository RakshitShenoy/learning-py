row=int(input("Enter the number of rows: "))

if(row %2==0):
    print("please enter a odd number")
else:
    row=int((row+1)/2)

    for i in range (row):
        for j in range(i+1):
            print("*",end=" ")
        print()
    row= row-1
    for i in range (row):
        for j in range(row-i):
            print("*",end=" ")
        print()    
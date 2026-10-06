import numpy as np 

a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
a.insert(5,67)
a[1:2]= [69,67]
a.remove(a[4])
# a.pop()
print(a)
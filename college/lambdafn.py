def multiply(x):
    result=x*2
    return result
list1=[1,2,3,4,5,6,7,8,9,10]
map(multiply,list1)
newlist=list(map(multiply,list1))
print(newlist)

newlist2=list(map(lambda y: y*2,list1))
print(newlist2)

p=0
n=0
n1=0
p1=0
while True:
    x=int(input())
    if x==0:
        break
    elif x>0:
        p+=1
        p1+=x
    
    else:
        n+=1
        n1+=x
        
print(p,n)        
print(p1,n1)

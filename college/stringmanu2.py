import re
txt=str(input("Enter a string: "))
upper=0
lower=0
digit=0
special=0

for i in range(len(txt)):
    
    if txt[i].isupper():
        print(txt[i],"is uppercase")
        print(i)
        upper+=1
    elif txt[i].islower():
        print(txt[i],"is lowercase")
        print(i)
        lower+=1
    elif txt[i].isdigit():
        print(txt[i],"is digit")
        print(i)
        digit+=1
    else:
        print(txt[i],"is special character")
        print(i)
        special+=1
print("Total characters in the string:", len(txt))
print("Uppercase count:", upper)
print("Lowercase count:", lower)
print("Digits count:", digit)
print("Special count:", special)
def kiosk():
    name=str(input("Enter your name: "))
    print(f"Hello, {name}!")
    bill=0
    order=[]
    while True:
        print(""" welcome to Burger King!
            1:burgers 50$
            2:fries 25$
            3:drinks 10$
            4:no thanks""")
        x=int(input("What would you like to order? "))
        if x in (1, 2, 3):
            q=int(input("How many would you like to order? "))

        if x==1:
            print("You ordered a burger!")
            order.append(("burger", q))
            print(f"Your order summary: {order}")
            bill+=50*q
            print(f"Your current bill is: ${bill}")
            print("do you want to add something else ?")
        elif x==2:
            print("You ordered fries!")
            order.append(("fries", q))
            print(f"Your order summary: {order}")
            bill+=25*q
            print(f"Your current bill is: ${bill}")
            print("do you want to add something else ?")
        elif x==3:
            print("You ordered a drink!")
            order.append(("drink", q))
            print(f"Your order summary: {order}")
            bill+=10*q
            print(f"Your current bill is: ${bill}")
            print("do you want to add something else ?")
        elif x==4:
            print("Thank you for your order!")
            print(f"Your order summary: {order}")
            print(f"Your total bill is: ${bill}")
            break
        else:
            print("Invalid option. Please try again.")  
kiosk()        
import random
print("""===================
Rock Paper Scissors
===================""")
print("""1) ✊
2) ✋
3) ✌️""")
choices= {1: "✊", 2: "✋", 3: "✌️"}
player = int(input("pick a number from 1-3:"))
if player not in choices:
    print("invalid input")
    exit()
computer = random.randint(1, 3)
print(f"you picked: {choices[player]}")
print(f"computer picked: {choices[computer]}")
diff=(player - computer)%3
if diff == 0:
    print("draw")
elif diff == 1:
    print("player wins")
else:
    print("computer wins")                                   
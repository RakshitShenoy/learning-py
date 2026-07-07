import random #start and importint of random module 
print("""===================
Rock Paper Scissors
===================""")#printing options for the user to choose from
print("""1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖""")
choices= {1: "✊", 2: "✋", 3: "✌️",4: "🦎", 5: "🖖"}#the five choices user can pick from
rules = {
    1: [3, 4],  # Rock crushes Scissors and crushes Lizard
    2: [1, 5],  # Paper covers Rock and disproves Spock
    3: [2, 4],  # Scissors cuts Paper and decapitates Lizard
    4: [2, 5],  # Lizard eats Paper and poisons Spock
    5: [1, 3]   # Spock vaporizes Rock and smashes Scissors
}
player = int(input("pick a number from 1-5:"))#players input
if player not in choices:
    print("invalid input")
    exit()
computer = random.randint(1, 5)#computer genrating a random number from 1-5 related to the game
print(f"you picked: {choices[player]}")#diplaying the players choice
print(f"computer picked: {choices[computer]}")#diplaying the computers choice

if player == computer:
    print("draw")
elif computer in rules[player]:
    print("player wins")
else:
    print("computer wins") #end       
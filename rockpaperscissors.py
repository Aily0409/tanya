import random

options = ["rock", "paper", "scissors"]


while True:
    user_ch = input("Choose rock, paper, scissors: ")
    computer_ch = random.choice(options)
    print(computer_ch)

    if user_ch == "quit":
        break

    if user_ch not in options:
        print("not allow")
        continue

    if user_ch == computer_ch:
        print("tie")
   
    elif (user_ch == "rock" and computer_ch == "scissors") or (user_ch == "paper" and computer_ch == "rock") or (user_ch == "scissors" and computer_ch == "paper"):
        print("Won")

    else:
        print("lose")
 
    
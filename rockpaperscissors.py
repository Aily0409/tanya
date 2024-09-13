import random

options = ["rock", "paper", "scissors"]

def star(text):
    a = "*"* 10
    b = "*" * 5
    print (f"{a}{text}{b}")

while True:
    user_ch = input("Choose rock, paper, scissors: ")
    computer_ch = random.choice(options)
    star(computer_ch)

    if user_ch == "quit":
        break

    if user_ch not in options:
        star("not allow")
        continue

    if user_ch == computer_ch:
        star("tie")
   
    elif (user_ch == "rock" and computer_ch == "scissors") or (user_ch == "paper" and computer_ch == "rock") or (user_ch == "scissors" and computer_ch == "paper"):
        star("Won")

    else:
        star("lose")
 
    
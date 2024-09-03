import random
while True : 
    T_number = random.randint(1,10)
    INVALID = 10
    guess = input (" ")
    if int(guess) < T_number :
        print ("Your guess is too low")
    if int(guess) > T_number:
        print ("Your guess is to high")
    if int(guess) == T_number:
        print ("You are correct!")
    if int(guess) > INVALID :
        print ("That number doesnt even exist")
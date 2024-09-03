guess = input ("Guess a number between 1 and 10:")
if int (guess)>3:print ("Your guess is too high")
if int (guess) ==3: print ("Your guess is correct!")
if int (guess) < 3: print ("Your guess is too low ")
INVALID = 10
if int (guess) > INVALID: print("Ummm... no, your guess is invalid")

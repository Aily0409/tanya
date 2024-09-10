import random
import time
 
def displayIntro():
     print('''You are in a land full of dragons. 
           In front of you, you see two caves. In one cave, 
           the dragon is friendly and will share his treasure 
           with you.The other dragon is greedy and hungry, and 
           will eat you on sight.''')
     print()

def chooseCave():
     cave = ''
     while cave != '1' and cave != '2':
         print('Which cave will you go into? (1 or 2)')
         cave = input()

     return cave

def story():
     print('You approach the cave...')
     time.sleep(2)
     print('It is dark and spooky...')
     time.sleep(2)
     print('A large dragon jumps out in front of you! He opens his jaws and...')
     print()
     time.sleep(2)

     friendlyCave = random.randint(1, 2)
     return friendlyCave

def ending(chosenCave, friendlyCave):
    if str(chosenCave) == str(friendlyCave):
        print('Gives you his treasure!')
        return True
    else:
        print('Gobbles you down in one bite!')
        return False
        
#def the_other_cave():  
    

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    friendlyCave = story()
    end = ending(caveNumber ,friendlyCave)
    if end == True:
        print('Do you want to play again? (yes or no)')
        playAgain = input()
    else:
        print("Do you want to see the other ending? (yes or no) ")
        answer = input()
        if answer == "yes":
            friendlyCave = story()
            end = ending(friendlyCave, friendlyCave)
            print("")
        else:
            break
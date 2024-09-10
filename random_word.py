import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
value= True
while(value):
    print("Hi! This program was made for you to guess some words")
    print("The words are python, java, javascript, ruby, html, and css")
    print(" ")
    user_guess= input("Make your guess!")
    if user_guess== selected_word:
        print("Yay! Congratulations! It turns out you are actually smart!")
    elif user_guess==selected_word:
        print ("Ermmm..no")
    print(" ")
    print(" ")

#Number Guessing Game
#Import modules
import random
from tkinter import *
from tkinter import messagebox

#Declare and initialise variables 
target = 0
score = 10
guess=0

#Define the clue functions
def add():
    return "The sum of target and guess is " + str(guess+target) 

def sub():
    return "The difference of target and guess is " + str(target-guess) 

def multiplication():
    return "The product of target and guess is " + str(guess*target)

def division():
    return "The division of target by guess is " + str(target/guess)

def greater_lesser():
    if target < guess:
        return 'Target is less than the guess'
    elif target > guess:
        return 'Target is greater than the guess'    
 
#Create the random clue generator
def clues():
    switcher = {
        0: add(),
        1: sub(),
        2: multiplication(),
        3: division(),
        4: greater_lesser()
        }
    return switcher.get(random.randint(0,4))

#Generate the target value
def generate_target_number():
    
    global target
    target = random.randint(1,50)
    messagebox.showinfo(message="Random Number Generated \nStart Guessing \nSTARTING SCORE=10")
    #Disable the random number button until game ends    
    random_number_button['state'] = DISABLED  
    #Activate the guessing button
    guess_button['state'] = NORMAL

#Guess and score by reading user input
def guess_and_score():
    #Make variables global for access across functions
    global score
    global guess
    try:
        guess =0 
        #Read if user submitted an input
        guess = int(guess_entry.get())
    except:
        messagebox.showerror(message="Enter a number to guess and play")
        return
    #If target and guess are the same, print score and prompt to user
    if guess == target:
        messagebox.showinfo(message="Congratulations!!! You guessed the number correct. Your score is "+str(score))
        #Enable random number button to play a new game and disable guessing button
        random_number_button['state'] = NORMAL
        guess_button['state'] = DISABLED  
        return
    #If the user runs out of guesses
    elif score == 0:
        messagebox.showwarning(message="Out of Guesses Buddy! Better luck next time );")
        return
    #Call the guessing functions to give the clues
    else:
        score -= 1
        message=clues()
        messagebox.showinfo(message=message)
        
#Create the user interface, specify the dimensions of the application window
window  = Tk()
window.geometry("350x200")
window.title("Number Guessing Game")

#Mention the title of the app
title_label = Label(window, text="Number Guessing Game\nGuess a number between 1 to 50", font=('Ubuntu Mono',12))
title_label.pack()

#Generate random number
random_number_button = Button(window, text="Generate Random Number", command=generate_target_number)
random_number_button.pack()
#Read User input
guess_label = Label(window, text="Enter your guess: ")
guess_label.pack()
guess_entry = Entry(window, width=3)
guess_entry.pack()
#Start guessing
guess_button = Button(window, text="Guess Me", command=guess_and_score, state=DISABLED)
guess_button.pack()
#Exit and close the app
window.mainloop()
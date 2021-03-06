# Using multi-line strings '''. So I don't have to use the \n 
# Using all caps for HANGMAN indicating a constant variable
# starting a tuple with the hangman drawing
# add time contraint 

import random #selecting a random word from a wordlist
import time # checking how long the user takes to guess the word
time1=time.time() #starting to count the seconds

HANGMAN = ('''  

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
WRONGMAX = len(HANGMAN) -1 #max of wrong guesses before gameover

WORDS = ("TUPLE", "CONDITIONAL", "PYTHON", "GITHUB", "TYPECASTING") #tuple of words that the user will guess from

word = random.choice(WORDS) #initiate the variables  (.choice pre-set function that will pick from the WORDS list)

until_now = "_" * len (word)   #how many letter are there in the word?

wrong = 0 #number of wrong guesses made

used = [] #empty list will contain all empty letters so no repeat

print "Are you really ready to play Python Hangman?? Let's go!!"  #this is where the program starts 

while wrong < WRONGMAX and until_now != word: 
    print HANGMAN[wrong] 
    print "\nThese are the letters you have already used:\n", used
    print "\nThis is the secret word that you have to guess..:\n\n", until_now

    guess = raw_input("\nPlease guess a letter:")
    guess = guess.upper() # everything bein compaired in caps

    while guess in used: # here we will know if the user already guessed the letter
        print "You have already guessed the letter:", guess
        guess = raw_input ("Guess a letter:")
        guess = guess.upper()
    used.append(guess)

    if guess in word: # is the letter guess in the word or not?
        print "\nYes", guess, "is in the word!"

        new = "" 
        for i in range(len(word)):
            if guess == word[i]: 
                new += guess
            else:
                new += until_now[i]
        until_now = new
    else:
        "\nSorry,", guess, "isn't in the word"
        wrong += 1 # will be increased by 1
if wrong == WRONGMAX:
    print HANGMAN(wrong)
    print "\nYou are dead..sorry:("
else:
    print "\nYou got lucky! You guessed it!"
print "\nThe secret word was", word

time2=time.time() # counting seconds stops here
totaltime=str(int(time2-time1)) # adding the start and finish of the time
print '\nWow it took you', totaltime, 'seconds!!!;)'
 

raw_input =("\n\nPress the enter key to exit.")

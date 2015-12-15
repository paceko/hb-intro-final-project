# hangmanpython imports a random word so import random
# Using multi-line strings '''. So I don't have to use the \n 
# Using all caps for HANGMANPYTHON indicating a constant variable
import random
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

WORDS = ("TUPLE", "CONDITIONAL", "PYTHON", "GITHUB", "TYPECASTING") #tuple of words

word = random.choice(WORDS) #initiate the variables

until_now = "_" * len (word)

wrong = 0 

used = [] #empty list will contain all empty letters so no repeat

print "Are you really ready to play Python Hangman??. Let's go!!"

while wrong < WRONGMAX and until_now != word: 
    print HANGMAN[wrong]
    print "\nThese are the letters you have already used:\n", used
    print "\nAnd the word that needs to be guessed is..:\n\n", until_now

    guess = raw_input("\nPlease enter your guess here:")
    guess = guess.upper()

    while guess in used: # here we will know if  already guessed the letter
        print "You have already guessed the letter:", guess
        guess = raw_input ("Enter a guess: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word: # is the guess in the word or not?
        print "\nYes", guess, "is in the word!"

        new = "" 
        for i in range(len(word)):
            if guess == word(i): 
                new += guess
            else:
                new += until_now[i]
        until_now = new
    else:
        "\nSorry,", guess, "isn't in the word"
        word += 1
if wrong == WRONGMAX:
    print HANGMAN(wrong)
    print "\nYou are dead..sorry:("
else:
    print "\nYou got lucky! You guessed it!"
print "\nThe word was", word

raw_input =("\n\nPress the enter key to exit.")

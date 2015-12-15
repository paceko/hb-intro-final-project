# hangman imports a random word so import random
# Using multi-line strings '''. So I don't have to use the \n 
# Using all caps for HANGMANPICTURES indicating a constant variable
import random
HANGMANPICTURES = ['''

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
    =========''']

word = 'github typecasting functions conditionals'.split() 

def Random_word(wordlist):  # this function returns a random string from the list of strings
    wordIndex = random.randint(0, len(wordlist)-1)  # first argument is 0 it goes tru the list until the last one -1

    return wordlist[word_index]

def Display(HANGMANPICTURES, missed_guess, correct_guess, secretword):
    print(HANGMANPICTURES[len(missed_guess)]) #this will display how many were wrong
    print()

    print ('missed_guess:')  
    for letter in missed_guess: #start of a for loop
    	print(letter)
    print()
    
    empty = '_' * len(secretword) # the operator * makes sure that empty has the same number of underscores as the secret word

    for i in range(len(secretword)):    # this will replace empty spots with guessed letters
    	if secretword[i] in correct_letter:
    		empty = empty[:i] + secretword[i] + empty[i+1:]

    for letter in empty: #spaces in between each of the letters from the secret word (volgens mij niet nodig!!)
    	print(letter)
    print()
 

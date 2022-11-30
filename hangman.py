# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent: near 24 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    lst_secret_word = set(secret_word)
    lst_letters_guessed = set(letters_guessed)
    if lst_letters_guessed.intersection(lst_secret_word) == lst_secret_word:
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = ""
    for x in secret_word:
        if x in letters_guessed:
          word = word + x
        else:
          word = word + ("_ ")
    return word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    alphabet_without = " "
    for el in alphabet:
        if el not in letters_guessed:
            alphabet_without = alphabet_without + el
    return alphabet_without
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    warning = 3
    guessed = 6
    letters_guessed = []
    vowels = list("aeiou")
    a = "--------------------"
    print(f"You have {warning} warnings left.")
    print("--------------------")
    print(f"You have {guessed} guessed left.")
    print(f"Available letters:  {string.ascii_lowercase}")
    while True:
      i = input("Please guess a letter: ")
      if i.isalpha() and i not in letters_guessed and len(i) == 1:
        if i in secret_word:
          letters_guessed.append(i)
          print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}\n--------------------")
          print(f"You have {guessed} guessed left.")
          print(f"Available letters: {get_available_letters(letters_guessed)}")
          get_guessed_word(secret_word, letters_guessed)
          if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! Your total score for this game is: {guessed*len(secret_word)}")
            break
        else:
          if i not in vowels:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")
            guessed -=1
            print(a)
            print(f"You have {guessed} guessed left.")
            print(f"Available letters: {get_available_letters(letters_guessed)}")
            if guessed < 1:
              print(f"Sorry, you ran out of guesses. The word was {secret_word}")
              break
          else:
            letters_guessed.append(i)
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")
            guessed -=2
            print(a)
            print(f"You have {guessed} guessed left.")
            print(f"Available letters: {get_available_letters(letters_guessed)}")
            if guessed < 1:
              print(f"Sorry, you ran out of guesses. The word was {secret_word}")
              break
      elif i in letters_guessed:
        if warning > 0:
          warning -= 1
          print(a)
          print(f"Oops! You've already guessed that letter. You have {warning} warnings left")
          print(get_guessed_word(secret_word, letters_guessed))
        else:
          guessed -= 1
          print(a)
          print(f"Oops! You've already guessed that letter. You have {guessed} guessed left")
          print(get_guessed_word(secret_word, letters_guessed))
          if guessed < 1: 
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
      elif i in letters_guessed and vowels:
        guessed -= 1
        print(a)
        print(f"Oops! You've already guessed that letter. You have {guessed} guessed left")
        print(get_guessed_word(secret_word, letters_guessed))
        if guessed < 1: 
          print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break

      elif not i.isalpha():
        if warning > 0:
          warning -= 1
          print(f"Oops! That is not a valid letter. You have {warning} warnings left")
        else:
          guessed -= 1
          print(a)
          print(f"Oops! That is not a valid letter. You have {guessed} guessed left")
          if guessed < 1: 
            print(a)
            print(f"Sorry, you ran out of guesses. The word was {secret_word}") 
            break
      elif len(i) != 1:
        if warning > 0:
          warning -= 1
          print(f"Oops! That is not a valid letter. You have {warning} warnings left")
        else:
          guessed -= 1
          print(a)
          print(f"Oops! That is not a valid letter. You have {guessed} guessed left")
          if guessed < 1:
            print(a)
            print(f"Sorry, you ran out of guesses. The word was {secret_word}") 
            break




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '') 
    if len(other_word) != len(my_word):
        return False
    for i in range(len(other_word)):
        if my_word[i] == "_":
            if my_word.count(other_word[i]) > 0:
                return False
            else:
                pass
        elif my_word[i] != other_word[i]:
            return False
    return True
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    some_word = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            some_word.append(i)
    if len(some_word) == 0:
        print("No matches found")
    else:
        for i in some_word:
            print(i, end=' ')





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    warning = 3
    guessed = 6
    letters_guessed = []
    vowels = list("aeiou")
    a = "--------------------"
    print(f"You have {warning} warnings left.")
    print("--------------------")
    print(f"You have {guessed} guessed left.")
    print(f"Available letters:  {string.ascii_lowercase}")
    while True:
      i = input("Please guess a letter: ")
      if i.isalpha() and i not in letters_guessed and len(i) == 1:
        if i in secret_word:
          letters_guessed.append(i)
          print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}\n--------------------")
          print(f"You have {guessed} guessed left.")
          print(f"Available letters: {get_available_letters(letters_guessed)}")
          get_guessed_word(secret_word, letters_guessed)
          if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! Your total score for this game is: {guessed*len(secret_word)}")
            break
        else:
          if i not in vowels:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")
            guessed -=1
            print(a)
            print(f"You have {guessed} guessed left.")
            print(f"Available letters: {get_available_letters(letters_guessed)}")
            if guessed < 1:
              print(f"Sorry, you ran out of guesses. The word was {secret_word}")
              break
          else:
            letters_guessed.append(i)
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")
            guessed -=2
            print(a)
            print(f"You have {guessed} guessed left.")
            print(f"Available letters: {get_available_letters(letters_guessed)}")
            if guessed < 1:
              print(f"Sorry, you ran out of guesses. The word was {secret_word}")
              break
      elif i == "*":
        print("Possible word matches are: ") 
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print()
        continue
      elif i in letters_guessed:
        if warning > 0:
          warning -= 1
          print(a)
          print(f"Oops! You've already guessed that letter. You have {warning} warnings left")
          print(get_guessed_word(secret_word, letters_guessed))
        else:
          guessed -= 1
          print(a)
          print(f"Oops! You've already guessed that letter. You have {guessed} guessed left")
          print(get_guessed_word(secret_word, letters_guessed))
          if guessed < 1: 
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
      elif i in letters_guessed and vowels:
        guessed -= 1
        print(a)
        print(f"Oops! You've already guessed that letter. You have {guessed} guessed left")
        print(get_guessed_word(secret_word, letters_guessed))
        if guessed < 1: 
          print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break

      elif not i.isalpha():
        if warning > 0:
          warning -= 1
          print(f"Oops! That is not a valid letter. You have {warning} warnings left")
        else:
          guessed -= 1
          print(a)
          print(f"Oops! That is not a valid letter. You have {guessed} guessed left")
          if guessed < 1: 
            print(a)
            print(f"Sorry, you ran out of guesses. The word was {secret_word}") 
            break
      elif len(i) != 1:
        if warning > 0:
          warning -= 1
          print(f"Oops! That is not a valid letter. You have {warning} warnings left")
        else:
          guessed -= 1
          print(a)
          print(f"Oops! That is not a valid letter. You have {guessed} guessed left")
          if guessed < 1:
            print(a)
            print(f"Sorry, you ran out of guesses. The word was {secret_word}") 
            break
      




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)



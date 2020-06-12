# Problem Set 2, hangman_with_hints.py
# Name: Amaan Ahmad

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
    # Making secret word into a list of letters
    secret_word_copy = list(secret_word)
    # Making a copy of list of letters in secret word
    secret_word_list = []
    # Removing duplicate letters
    for a in secret_word_copy:
      if a not in secret_word_list:
        secret_word_list.append(a)
    # For loop checking if guessed letters are in the secret word and removing them
    for x in letters_guessed:
        if x in secret_word_list:
            secret_word_list.remove(x)
    if len(secret_word_list) == 0:
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
    
    # Making secret word into a list of letters
    secret_word = list(secret_word)
    # Making list to which will become a list for placeholders
    empty_word = list(secret_word)
    # Making a copy of list of letters in secret word
    # List of all possible letters to guess
    letters_available = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Making a list of placeholders for secret word
    for n, i in enumerate(secret_word):
      if i in letters_available:
        empty_word[n] = '_ '
    # For loop checking if guessed letters are in the secret word and removing them
    for m, j in enumerate(secret_word):
      if j in letters_guessed:
        empty_word[m] = secret_word[m]
    return ''.join(empty_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # List of all possible letters to guess
    letters_available = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Checks removes any letter guessed from letters
    for x in letters_available:
      if x in letters_guessed:
        letters_available.remove(x)
    return ''.join(letters_available)

def total_score(secret_word, guesses):
    '''
    secret_word: string, the word the user is guessing
    guesses: int, number of guesses left
    returns: int, Total score = guesses * number unique letters in secret_word
    '''
    # Convert string secret word into list
    secret_word = list(secret_word)
    # List of unique letters in secret word
    unique = set(secret_word)
    # return total score
    return len(''.join(unique))*guesses

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # Remove spaces as will count as extra list items
    my_word = my_word.replace(' ', '')
    # Initialise bool for if word matches
    match = False
    # If lengths are different, cannot match
    if len(my_word) != len(other_word): #check length of words first; lengh must ==
      return False
    else:
      # Check if letters in same places except gaps
      for i in range(len(my_word)):
        if my_word[i]!= '_' and my_word[i] == other_word[i]:
          match = True
        # Not a gap and doesn't match
        elif my_word[i]!= '_' and my_word[i] != other_word[i]:
          match = False
          break
    return match

def show_possible_matches(my_word, wrong_guesses):
    '''
    my_word: string, with _ characters, current guess of secret word
    wrong_guesses: list, with letters guessed not in secret_word
      lowercase
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # Initialise string of matched words
    matched_words = ''

    # Check if word in wordlist_short includes wrong guesses
    for x in wordlist:
      include_wrong_guess = False
      if match_with_gaps(my_word, x):
        # 'x' should not include one of the wrong guesses, checks letters
        for y in wrong_guesses:
          if y in x:
            include_wrong_guess = True
            break
        if not(include_wrong_guess):
          matched_words += x + ' '

    if matched_words == '':
      matched_words = 'No matches found!'

    # Output matched words
    return matched_words        

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
    
    guesses = 6                       # Total number of guesses
    letters_guessed = []              # Intialising list for letters_guessed
    wrong_guesses = []                # Initialising list of wrong guesses
    valid = 1                         # Used to trigger while loop if wrong input
    warning = 3                       # Warnings for wrong input
    word = list(secret_word)          # List version of secret_word
    vowels = ['a','e','i','o','u']    # List of vowels

    # Intro to game, telling user, the length of word, available guesses and number of guesses left
    print("*** Welcome to the game Hangman! ***")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    print("You have", guesses, "guesses left.")
    
    # Cycle runs whilst user still has guesses
    while guesses > 0:
      while valid == 1:
        print("Available letters are", get_available_letters(letters_guessed))
        x = input("Please guess a letter: ",)
        x.lower()
        # If user is asking for hints
        if x == '*':
          print(show_possible_matches(get_guessed_word(word, letters_guessed), wrong_guesses))
          print("---------------")
          # Loop repeats
          valid = 1
        # If input not a valid guess
        elif x not in get_available_letters(letters_guessed):
          print("Oops! That is not a valid letter. You have", warning, "warnings left:", get_guessed_word(word, letters_guessed))
          print("-------------")
          warning -= 1
          # Loop repeats
          valid = 1
          # Checks if warning is 0 and removes a guess, replenishes warnings
          if warning == 0:
            print("Oops! You have no warnings left so you lose one guess :(, You now again have 3 warnings:")
            guesses -= 1
            warning = 3
        # User guesses a letter
        else:
          break
        # If no guesses left due to warnings
      if guesses == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word+".")
        break
      else:
        letters_guessed.append(x)
        # Guess is correct
        if x in word:
          print("Good Guess:", get_guessed_word(word, letters_guessed))
        # Wrong guess and guess is a vowel
        elif x not in word and x in vowels: 
          wrong_guesses.append(x)
          print("Oops! That letter is not in my word:", get_guessed_word(word, letters_guessed))
          guesses -= 2
          print("For a hint, press '*'")
        # Wrong guess and guess is a consonant
        else: 
          wrong_guesses.append(x)
          print("Oops! That letter is not in my word:", get_guessed_word(word, letters_guessed))
          guesses -= 1
          print("For a hint, press '*'")

        print("-------------")
        # Check if word is guessed
        if is_word_guessed(secret_word, letters_guessed):
          print("Congratulations, you won! The word was indeed: ", secret_word)
          # Total Score
          print("Your total score for this game is: ", total_score(word, guesses))
          break
        # Prints number of guesses left
        if guesses>0:
          print("You have", guesses, "guesses left.")
        # No guesses left
        else: 
          print("You have 0 guesses left.")
        # Check if word is guessed
          print("Sorry, you ran out of guesses. The word was", secret_word+".")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass
  
  play_again = True
  # Play again loop
  while play_again:
      secret_word = choose_word(wordlist)
      hangman_with_hints(secret_word)
      user_input = input('Do you wanna play more (Y/N)? ')
      if str.lower(user_input) != 'y' :
          play_again = False

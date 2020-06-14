def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand, including wildcards. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # Copy hand so function doesn't mutate hand
    hand_copy = hand.copy()
    # Create list of possible words formed
    possible_words = []
    # Creat a list for valid words
    valid_words = []
    # Check for wildcard
    if '*' in word.lower():
        # Check if wildcard, when replaced with a vowel, makes a valid word
        for vowel in VOWELS:
            word_check = word.lower()
            word_check = word_check.replace('*', vowel)
            possible_words.append(word_check)
    else:
        # Check word in word list
        possible_words.append(word.lower())
    # Check words in possible_words
    for possible in possible_words:
        if possible in word_list:
            valid_words.append(possible)
            break
    # Check if words in valid words:
    if len(valid_words) == 0:
        return False
    # Checks in letters in hand
    for letter in word.lower():
        if letter not in hand_copy:
            return False
        else:
            hand_copy[letter] -= 1
    for letter in word.lower():
        if letter in hand_copy:
            # Word is valid
            if hand_copy[letter] >= 0:
                return True
            # Not enough letters in hand to make up word
            else:
                return False

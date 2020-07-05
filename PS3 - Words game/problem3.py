def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    new_hand = hand.copy()
    # Check word in word list
    if word.lower() not in word_list:
        return False
    # Check letters of word are in hand
    else:
        for letter in word.lower():
            if letter not in hand:
                break
            else:
                new_hand[letter] -= 1
        for letter in word.lower():
            if letter in hand:
                # Word is valid
                if new_hand[letter] >= 0:
                    return True
                # Not enough letters in hand to make up word
                else:
                    return False
            # Letter not in hand
            else: 
                return False
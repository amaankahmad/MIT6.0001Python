def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Initialise new_hand variable that is a dictionary
    new_hand = hand.copy()
    # Check if letters in word are in hand
    for letter in word.lower(): 
        if letter in new_hand:
            # Check that dictionary values are all greater than 0 or removed
            if new_hand[letter] == 1:
                del(new_hand[letter])
            elif new_hand[letter] > 1:
                new_hand[letter] -= 1
    # Return new_hand that is a dictionary
    return new_hand

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
new_hand = update_hand(hand, 'quail')
print (new_hand)

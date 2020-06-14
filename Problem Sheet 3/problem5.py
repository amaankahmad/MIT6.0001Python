def play_hand(hand, word_list):
    
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print("Current Hand: ",display_hand(hand))
        # Ask user for input
        user_input = input(print('Enter your word, or "!!" to indicate that you are finished:'))
        # If the input is two exclamation points:
        if user_input == '!!':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_input, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                score += get_word_score(user_input, calculate_handlen(hand))
                print('"'+user_input+'" earned '+get_word_score(user_input, calculate_handlen(hand))+' points. Total:',score+'points')
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_input)
    # Game is over (user entered '!!' or ran out of letters),
    if calculate_handlen(hand) == 0:
        print("Ran out of letters.")
    # so tell user the total score
    print("Total score:",score,"points!")
    # Return the total score as result of function
    return score
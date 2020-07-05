def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    # Convert word string into lower case only
    word = word.lower()
    # Initialise length of word variable
    word_length = len(word)
    # First component: Sum of the points for letters in the word
    firstComponent = 0 # Initialise variable
    for letter in word:
        firstComponent +=SCRABBLE_LETTER_VALUES[letter]
    print(firstComponent)
    # Second component: 1 or 7*wordlen - 3*(n-wordlen)  
    secondComponent = 7*word_length - 3*(n-word_length)
    if secondComponent < 1:
        secondComponent = 1
    print(secondComponent)
    return firstComponent*secondComponent

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
word = 'apple'
n = 7

print(get_word_score(word, n))
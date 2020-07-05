# Problem Set 4A
# Name: Amaan Karim Ahmad

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Initialise list of permutations
    permutations_list = []
    # Base case of one letter sequence
    if len(sequence)==1:
        return sequence
    # Recursively call remaining letters
    permutations = get_permutations(sequence[1:])
    # Store character being moved across
    char = sequence[0]
    for permutation in permutations:
        for letter in range(len(permutation)+1):
            # Moving char across remainder of sequence
            permutations_list.append(permutation[:letter]+char+permutation[letter:])
    # Return all permutations
    return permutations_list

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abcd'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    



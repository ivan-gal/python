def isIn(char, str):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    str = ''.join(sorted(str))
    if char != str and len(str) == 1 or len(str) == 0:
        return False
    if char == str[len(str) // 2]:
        return True
    if char > str[len(str) // 2]:
        return isIn(char, str[len(str) // 2: len(str) - 1])
    if char < str[len(str) // 2]:
        return isIn(char, str[0: len(str) // 2])


print(isIn('a', 'zapato'))

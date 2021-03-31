
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.


def alphabet_position(text):
    bad_chars = [';', ':', '!', ".", "'", ]
    for chr in bad_chars:
        text = text.replace(chr, '')
    newString = ''
    for c in text.lower():
        if c != ' ' and c >= a:
            newString += str(ord(c) - 96) + ' '
    return newString[:-1]


print(alphabet_position('Aola joputa'))

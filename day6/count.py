animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    maxLen = 0
    maxAnimal = []
    for animals in aDict.values():
        if len(animals) > maxLen:
            maxLen = len(animals)
            maxAnimal = animals

    for k in aDict.keys():
        if aDict[k] == maxAnimal:
            return k


print(biggest(animals))

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    totalAnimal = 0
    for animals in aDict.values():
        if isinstance(animals, tuple) or isinstance(animals, list):
            totalAnimal += len(animals)
        else:
            totalAnimal += 1
    return totalAnimal


print(how_many(animals))

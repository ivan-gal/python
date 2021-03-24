tulipan = ('I', 'am', 'a', 'test', 'tuple')


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for c in range(0, len(aTup), 2):
        newTup = newTup + (aTup[c],)
    return newTup


print(oddTuples(tulipan))

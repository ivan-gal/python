def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    prod = 1
    for n in range(exp):
        prod *= base
    return prod


print(iterPower(2, 4))

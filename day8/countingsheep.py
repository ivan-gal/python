# Consider an array/list of sheep where some sheep may be missing from
# their place. We need a function that counts the number of sheep present
# in the array(true means present).

# For example,

# [True,  True,  True,  False,
#  True,  True,  True,  True,
#  True,  False, True,  False,
#  True,  False, False, True,
#  True,  True,  True,  True,
#  False, False, True,  True]


def count_sheeps(sheep):
    # TODO May the force be with you
    sheepNumber = 0
    for sh in sheep:
        if sh:
            sheepNumber += 1
    return sheepNumber

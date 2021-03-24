

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(min, max, word, ) = get_data(
    ((1, 'mine'), (2, 'pepe'), (3, 'chapata'), (4, 'zapatilla')))

print(min)

print(max)

print(word)

# del(list[index]) remove item from index
# list.remove(item) search for items and remove, if it doesn't exist returns an error.
# list.pop() pop last item and return it
# list(s) String to List // string.split() same as js // string.join()
# list.sort() return list mutated // list.sorted() doesnt mutate  // list.reverse() reverse list

print(abs(3.0))
print(len(range(0, 6)))

my_dict = {}
grades = {'Ana': 'B', 'Juan': 'C', 'Denise': 'B', 'Jona': 'A++'}
grades['Mary'] = 'F'
del(grades['Juan'])

print('Ana' in grades)
print(grades.keys())

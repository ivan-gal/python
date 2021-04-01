def genPrimes():
    primeList = [2, ]

    for prime in range(2, 1000):
        num = 0
        for n in primeList:
            if prime % n == 0:
                num += 1
        if num == 0:
            primeList.append(prime)
            yield prime


f = genPrimes()

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

x = 64
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high = ', high, ' ans = ', ans)
    numGuesses += 1
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ', numGuesses)
print(str(ans) + 'is close to square root of ' + str(x))



def fibSlow(n):
    global numFibCalls
    if n == 1:
        numFibCalls += 1
        return 1
    elif n == 2:
        numFibCalls += 1
        return 2
    else:
        numFibCalls += 1
        return fibSlow(n-1) + fibSlow(n-2)


def fibFast(n, d):
    if n in d:
        return d[n]
    else:
        ans = fibFast(n-1, d) + fibFast(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}
numFibCalls = 0

print(fibSlow(15))
print(numFibCalls)

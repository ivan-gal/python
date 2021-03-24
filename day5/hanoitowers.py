def printMove(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))


def hanoi_tow(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        hanoi_tow(n-1, fr, spare, to)
        hanoi_tow(1, fr, to, spare)
        hanoi_tow(n-1, spare, to, fr)


hanoi_tow(10, 'F1', 'F2', 'F3')

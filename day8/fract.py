class Fraction (object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + ' / ' + str(self.denom)


three_eights = Fraction(3, 8)

print(three_eights)

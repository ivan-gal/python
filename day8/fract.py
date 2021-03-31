class Fraction (object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + ' / ' + str(self.denom)

    def getNumber(self):
        return self.num

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numberNew = other.getDenom() * self.getNumber() \
            + other.getNumber() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numberNew, denomNew)

    def __sub__(self, other):
        numberNew = other.getDenom() * self.getNumber() \
            - other.getNumber() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numberNew, denomNew)


three_eights = Fraction(3, 8)
one_half = Fraction(1, 2)

print(three_eights.__add__(one_half))

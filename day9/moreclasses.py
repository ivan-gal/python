import datetime


class Person(object):
    def __init__(self, name):
        """CREATE A PERSONA CALLED NAME"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def __str__(self):
        return (self.name)

    def setBirthday(self, day, month, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName


juanito = Person('Juanito García')

juanito.setBirthday(20, 2, 1994)
print(juanito.getAge())

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


class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, word):
        return (self.getLastName() + " says : " + word)


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, word):
        return MITPerson.speak(self, "Dude, " + word)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, word):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + word)

    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)


Louis = MITPerson('Fernando Gomez')
joseL = MITPerson('Fuck you man')

jose_fernando = Professor('Jose Fernando', 'Matematicas')

mattD = UG("Matt Damon", 2020)
lowerL = UG("Lower Leis", 2019)
bigD = UG("Big David", 2017)

print(lowerL.speak("Wow this sucks"))
print(bigD.speak("wooo don't be a David"))

Louis.setBirthday(20, 12, 1930)

print(bigD.getClass())

print(isStudent(bigD))

print(jose_fernando.speak('las matematicas'))
print(jose_fernando.lecture('matematicas'))

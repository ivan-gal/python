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


class Grades (object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    # """Assumes grade is a float
    # Add Gracde to the list of grades for student"""

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
            print(self.students)
        return self.students[:]


def gradeReport(course):
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + "\' mean grade is " + str(average))

        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


year20 = Grades()

year20.addStudent(bigD)
year20.addStudent(lowerL)
year20.addStudent(mattD)

year20.addGrade(bigD, 83.5)
year20.addGrade(bigD, 32.5)
year20.addGrade(bigD, 42.5)

year20.addGrade(lowerL, 83.5)
year20.addGrade(lowerL, 32.5)
year20.addGrade(lowerL, 42.5)


year20.addGrade(mattD, 83.5)
year20.addGrade(mattD, 32.5)
year20.addGrade(mattD, 42.5)

print(gradeReport(year20))

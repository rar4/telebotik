import datetime as dat
a = 0
class Human:
    d = 0
    def find_date(self=0):
        date = str(dat.datetime.now())
        data = date.split()
        date = data[1]
        return date
    date = find_date(d)

    def __init__(self, name, lname, floor, age, sens, love=[],  friends=['none']):
        self.name = name
        self.lname = lname
        self.friends = friends
        self.floor = floor
        self.age = age
        self.sens = sens
        self.love = love

    def __str__(self):
        nameee = {'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends}
        return str(nameee)


    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.love]
        return list


    def __add__(self, other):
        if type(self) == type(other):
            fgf = 9
            for i in other.friends:
                if i == self.__repr__():
                    fgf = 0
            if 'none' in self.friends:
                self.friends.remove('none')
            if 'none' in other.friends:
                self.friends.remove('none')
            if fgf == 9:
                self.friends.append(other.__repr__())
                other.friends.append(self.__repr__())
                return f'{other.name} is now your friend'
            return 'you have already have such friend'
        return 'you can not be friends'

class Child(Human):
    def __init__(self, name, lname, floor, age, sens,  toys=None, *args, **kwargs):
        super().__init__(name, lname, floor, age, sens)
        self.toys = toys
    def __str__(self):
        nameee = {'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends, "toys": self.toys}
        return str(nameee)


    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.love, self.toys]
        return list

    def game(self):
        if self.toys == 'cubes':
            return 'i`m building a tower'
        if self.toys == 'guitar':
            return 'IM MAKING MUSIK'
        else:
            return f'I`m plaing with {self.toys}.'

class Adult(Human):
    def __init__(self, name, lname, floor, age, sens, love='he has not love',  friends=['none'] ):
        super().__init__( name, lname, floor, age, sens)

    def __str__(self):
        nameee = str({'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends})
        return nameee

    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens,]
        return list

    def __sub__(self, other):
        if type(self) == type(other):
            fgf = 9
            for i in other.friends:
                if i == self.__repr__():
                    fgf = 0
            if fgf == 0:
                other.friends.remove(self.__repr__())
                self.friends.remove(other.__repr__())
                return 'he or she is not your friend now'
            return 'you haven`t such friend'
        return 'error'
    def __mul__(self, other):
        if type(self) == type(other):
            fgf = 9
            for i in other.love:
                if i == self.__repr__():
                    fgf = 0
            if fgf == 9:
                other.love.append(self.__repr__())
                self.love.append(other.__repr__())
                return f'your love is {other.name}'
            return 'you have already love him or her'
        return 'error'

    def __floordiv__(self, other):
        if type(self) == type(other):
            fgf = 9
            for i in other.love:
                if i == self.__repr__():
                    fgf = 0
            if fgf == 0:
                other.love.remove(self.__repr__())
                self.love.remove(other.__repr__())
                return f'your love is not {other.name}'
            return 'you do not love him or her'
        return 'error'

class Student(Adult):
    def __init__(self, name, lname, floor, age, sens, clas=None, *args, **kwargs):
        super().__init__(name, lname, floor, age, sens)
        self.clas = clas

    def __str__(self):
        nameee = {'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends, 'clas' : self.clas}
        return str(nameee)

    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.clas]
        return list

class Test:


    def __init__(self, teacher):
        a = 9
        tst = {}
        while a != 100:
            try:
                a = int(input('what do you want to do? (1 - make a question, 0 - finish): '))
            except:
                pass
            if a == 1:
                d =  input('input a question: ')
                l = input('input an answer: ')
                tst[d] = l
            if a == 0:
                self.test = tst
                self.clas = teacher.clas
                return

    def do_test(self, student):
        if self.clas == student.clas:
            mark = 0
            max_mark = 0
            for i in self.test.items():
                max_mark += 1
                question, answer = i[0], i[1]
                student_answer = input(f'{question}: ')
                if answer == student_answer:
                    mark += 1
            return f'you recived {mark} from {max_mark}'
        return f'you are not in {self.clas}'

class Worker(Adult):
    increace_amount = 1.06
    def __init__(self, name, lname, floor, age, sens, salary):
        super().__init__(self, name, lname, floor, age, sens)
        self.salary = salary
    def pay_increace(self):
        self.salary *= Worker.increace_amount

class Teacher(Worker):
    def __init__(self, name, lname, floor, age, sens, salary, clas):
        super().__init__(name, lname, floor, age, sens, salary)
        self.clas = clas

class ElementaryShcoolStudent(Student, Child):
    def __init__(self,  name, lname, floor, age, sens, clas, game, toys):
        super().__init__(name, lname, floor, age, sens,  clas,  toys)
        self.game = game
    def plaing_game(self):
        return f'i`m plaing in{self.game}'

    def __str__(self):
        nameee = {'name': self.name, 'last name': self.lname, 'sex': self.floor, 'age': self.age,
                  'sens of life': self.sens, 'love': self.love, 'friends': self.friends, 'clas': self.clas,
                  'game' : self.game, "toy" : self.toys}
        return str(nameee)

    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.clas, self.toys, self.game]
        return list





def main():
    print('------------------------------')
    child1 = Child('alie', 'ivanv','femail', '11', 'be a friend', 'guitar')
    print('------------------------------')
    child2 = Child('ali', 'ivanov','mail', '11', 'be a friend', 'cubes')
    print('------------------------------')
    print(child2)
    print('------------------------------')
    print(child1)
    print('------------------------------')
    print(child1.game())
    print('------------------------------')
    print(child2.game())
    print('------------------------------')
    print(child2 + child1)
    print('------------------------------')
    print(child2.friends)
    print('------------------------------')
    adult1 = Adult('alie', 'ivanv', 'femail', '11', 'be not a friend')
    print('------------------------------')
    adult2 = Adult('ali', 'ivanov', 'mail', '11', 'be not a friend')
    print('------------------------------')
    print(adult2)
    print('------------------------------')
    print(adult1)
    print('------------------------------')
    print(adult2+adult1)
    print('------------------------------')
    print(adult2.friends)
    print('------------------------------')
    print(adult2 - adult1)
    print('------------------------------')
    print(adult2.friends)
    print('------------------------------')
    print(adult2 * adult1)
    print('------------------------------')
    print(adult2.love)
    print('------------------------------')
    print(adult2 // adult1)
    print('------------------------------')
    print(adult2.love)
    student1 = Student('al', 'ivana', 'femail', '11', 'be not a friend', '11q')
    teacher1 = Teacher('ali', 'ivanov', 'mail', '11', 'be not a friend', 30000, '11q')
    teacher2 = Teacher('ali', 'ivanov', 'mail', '11', 'be not a friend', 30000, '10q')
    test = Test(teacher1)
    tests = Test(teacher2)
    print(test.do_test(student1))
    print('------------------------')
    print(tests.do_test(student1))
asdds=ElementaryShcoolStudent('a','a','a,','a,','a','a','a', 'a')
print(asdds )
main()
#вибачте, у мене проблема з другим дз в наслідуванні, в класі ElementaryShcoolStudent я наслідую два класи і в ініті
# у мене повертає помилку, на скільки я зрозумів, програма не бачить аргумент, який є у одного класу, а у іншого - ні

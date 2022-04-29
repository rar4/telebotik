import datetime as dat
a = 0
class Human:
    d = 0
    def date(self=0):
        date = str(dat.datetime.now())
        data = date.split()[0]
        return data
    def __init__(self, name, lname, floor, sens, love=[],  friends=['none']):
        self.date_birdhday = self.date()
        self.name = name
        self.lname = lname
        self.friends = friends
        self.floor = floor
        self.sens = sens
        self.love = love
    @property
    def age(self):
        if self.name == None:
            return None
        now_str = str(dat.datetime.now())
        date = now_str.split()[0]
        year, month, day = date.split('-')
        year_bir = self.date_birdhday.split('-')[0]
        year_bir = int(year_bir)
        year = int(year)
        age = year - year_bir
        return age

    @age.deleter
    def age(self):
        self.age = None

    @age.setter
    def age(self, age):
        if age == None:
            self.date_birdhday = None
            return
        years, month, day = self.date_birdhday.split('-')
        now_str = str(dat.datetime.now())
        now_str = now_str.split()[0]
        date = int(now_str.split('-')[0])
        years = date - age
        self.date_birdhday = f'{years}-{month}-{day}'

    @property
    def pasport(self):
        if self.name == None:
            return None
        strin = len(f'{self.name}     {self.lname}') - len(f'{self.floor}')
        len_strin = len(f'{self.name}     {self.lname}')
        space = ''
        string = ''
        spaces = ''
        sp = ''
        for i in range(0 , strin):
            string += ' '
        for i in range(0, len(f'{self.name}     {self.lname}-')):
            spaces += '-'
        for i in range(0, len_strin- len(str(self.age))):
            space += ' '
        pasport = f'{spaces}\n' \
                  f'{self.name}     {self.lname}-\n' \
                  f'' \
                  f'{self.floor}{string}-\n' \
                  f'{self.age}{space}-\n' \
                  f'{spaces}\n' \
                  f'sens : {self.sens}   {space}\n\n\n'
        return pasport

    @pasport.setter
    def pasport(self,list):
        self.name = list[0]
        self.lname = list[1]
        self.floor = list[2]
        self.age = list[3]
        self.sens = list[4]

    @pasport.deleter
    def pasport(self):
        self.name = None
        self.lname = None
        self.floor = None
        self.age = None
        self.sens = None

    def __str__(self):
        nameee = {'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends, 'date of birth': self.date}
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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.love]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]
class Child(Human):
    def __init__(self, name, lname, floor,sens,  toys=None, *args, **kwargs):
        super().__init__(name, lname, floor, sens)
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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.love, self.toys]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]
class Adult(Human):
    def __init__(self, name, lname, floor, sens):
        super().__init__( name, lname, floor, sens)

    def __str__(self):
        nameee = str({'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends})
        return nameee

    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens]
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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]
class Student(Adult):
    def __init__(self, name, lname, floor, sens, clas=None, *args, **kwargs):
        super().__init__(name, lname, floor, sens)
        self.clas = clas

    def __str__(self):
        nameee = {'name' :self.name, 'last name': self.lname, 'sex': self.floor, 'age' : self.age, 'sens of life': self.sens, 'love': self.love, 'friends': self.friends, 'clas' : self.clas}
        return str(nameee)

    def __repr__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.clas]
        return str(list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.clas]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]
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
    def __init__(self, name, lname, floor, sens, salary):
        self.salary = salary
        super().__init__(name, lname, floor, sens)
    def pay_increace(self):
        self.salary *= Worker.increace_amount

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.salary]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]



class Teacher(Worker):
    def __init__(self, name, lname, floor, sens, salary, clas, students):
        super().__init__(name, lname, floor, sens, salary)
        self.clas = clas
        for i in students:
            if str(type(i)) != "<class '__main__.Student'>":
                students = None
        self.students = students
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.salary, self.clas, self.students]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]

class ElementaryShcoolStudent(Student, Child):
    def __init__(self,  name, lname, floor, sens, clas, game, toys):
        super().__init__(name, lname, floor, sens,  clas,  toys)
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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        list = [self.name, self.lname, self.floor, self.age, self.sens, self.clas, self.game, self.toys]
        if self.index >= len(list):
            raise StopIteration
        index = self.index
        self.index += 1
        return list[index]
def main():
    alex=Human('Alex', 'Mishchenko', 'male', 'have a pasport')
    alex=Human('Alex', 'Mishchenko', 'male', 'have a pasport')
    print(alex.__repr__())
    alex.age = 19
    print(alex.__repr__())
    print(alex.pasport)
    alex.pasport = ['Adis', 'Abeba', 'female', 12, 'change a pasport']
    print(alex.pasport)
    print(alex.name)
    print(alex.__repr__())
    del alex.pasport
    print(alex.pasport)
    print(alex.__repr__())
    alex=Child('Ale', 'chenko', 'male', 'have a pasport', 'guitar')
    print(alex.pasport)
alex = Human('alx', 'ali', 'mail', 'iter')
for i in alex:
    print(i)
print('--------------------------')
alex = Child('alx', 'ali', 'mail', 'iter', 'cube')
for i in alex:
    print(i)
print('--------------------------')
alex = Student('alx', 'ali', 'mail', 'iter', '6b')
for i in alex:
    print(i)
print('--------------------------')
alex = Worker('alx', 'ali', 'mail', 'iter', 100)
for i in alex:
    print(i)
print('--------------------------')
lex = Student('alx', 'ali', 'mail', 'iter', '6b')
alex = Teacher('alx', 'ali', 'mail', 'iter', 100, '6b', [lex])
for i in alex:
    print(i)
print('--------------------------')
alex = ElementaryShcoolStudent('alx', 'ali', 'mail', 'iter', '6b', 'Minecraft', 'cube')
for i in alex:
    print(i)
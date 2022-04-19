import datetime as dat
from functools import wraps



def time_logger(funk):
    import time
    @wraps(funk)
    def tim(*args, **kwargs):
        tim1 = time.time()
        result = funk(*args, **kwargs)
        tim2 = time.time()
        timerr = f'time of function is {tim2 - tim1} seconds'
        with open('log.txt', 'a') as log:
            log.write(timerr)
            log.write(' name is ')
            log.write(funk.__name__)
            log.write('\n')
        return result
    return tim



def info_loger(funk):
    def tim(*args, **kwargs):
        result = funk(*args, **kwargs)
        with open('logg.txt', 'a') as log:
            log.write(f' acction -- {funk.__name__}')
            nam = funk.__name__
        if nam == 'credit_to_card':
            with open('logg.txt', 'a') as log:
                log.write(f' number -- {Bancomat.nummm}  ')
                log.write(f'money -- {Bancomat.money}\n')
        if nam == 'withdraw':
            with open('logg.txt', 'a') as log:
                log.write(f' pin -- {Bancomat.pin}  ')
                log.write(f'money -- {Bancomat.money}\n')
        else:
            with open('logg.txt', 'a') as log:
                log.write(f' cvv -- {Bancomat.cvv}, date -- {Bancomat.date}, reciver -- {Bancomat.an_ac}\n')
        return result

    return tim


class BankAcount:
    nums = []
    @staticmethod
    def date():
        a = str(dat.datetime.now()).split()
        a = a[0]
        a = a.split('-')
        a = f'{a[1]}/{a[2]}'
        return a
    def __init__(self,name, pin, number, cvv, money=0):
        for i in BankAcount.nums:
            if i == number:
                print('this number is already exists')
                return
        self.ame = name
        self.__pin = pin
        self.num = number
        self.__cvv = cvv
        self._dat = BankAcount.date()
        self.__money = money
        BankAcount.nums.append(number)
    @info_loger
    def print_money(self, pin):
        if self.__pin == pin:
            return self.__money
    @info_loger
    @time_logger
    def credit_to_card(self, num, money):
        if num == None:
            return num
        if self.num == num:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @info_loger
    @time_logger
    def withdraw(self, pin, money):
        if self.__pin == pin:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @info_loger
    @time_logger
    def trans_to_card(self, another_acount, cvv, date, money):
        if self.__cvv == cvv and self._dat == date:
            self.__money += money
            another_acount.__money -= money
            return 'transacttion complited'
        else:
            return 'error'
class Bancomat:
    date = 0
    nummm = 0
    cvv = 0
    pin = 0
    an_ac = 0
    money = 0
    @staticmethod
    def print_money(acount):
        try:
            pin = int(input('input a pin: '))
        except:
            return 'it is not number'
        return BankAcount.print_money(acount, pin)

    @staticmethod
    @time_logger
    def credit_to_card(acount):
        try:
            num = int(input('input a number: '))
        except:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
        except:
            return 'it is not number'
        Bancomat.nummm = num
        Bancomat.money = money
        return acount.credit_to_card(num, money)

    @staticmethod
    @time_logger
    def withdraw(acount):
        try:
            pin = int(input('input a pin: '))
        except:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
            money = money * -1
        except:
            return 'it is not number'
        Bancomat.pin = pin
        Bancomat.money = money * -1
        return acount.withdraw(pin, money)
    @staticmethod
    @time_logger
    def trans_to_card(acount, another_ack):
        try:
            date = input('date: ')
            cvv = int(input('cvv: '))
        except:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
            money = money * -1
        except:
            return 'it is not number'
        Bancomat.money = money * -1
        Bancomat.cvv = cvv
        Bancomat.date = date
        Bancomat.an_ac = another_ack.ame
        return acount.trans_to_card(another_ack, cvv, date, money)




def main(ded, vnuk):
    a = 0
    while a != 235.5:
        try:
            a = int(input('what do you want to do? (1 -- credit to card, 2 -- withdraw, 3 -- trans out of card, 4 -- chek balanse, 5 -- finish ) '))
        except:
            print('it is not a number')
        if a == 1:
            print(Bancomat.credit_to_card(ded))
            print('a')
        if a == 2:
            print(Bancomat.withdraw(ded))
        if a == 3:
            print(Bancomat.trans_to_card(ded, vnuk))
        if a == 4:
            print(Bancomat.print_money(ded))
        if a == 5:
            return

ded = BankAcount('ded', 2283, 8753267899876535, 478)
vnuk = BankAcount('vnuk', 2285, 9753267899876535, 487)
main(ded, vnuk)

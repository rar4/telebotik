import datetime as dat
from functools import wraps



def logger(funk):
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



def loger(funk):
    def tim(*args, **kwargs):
        result = funk(*args, **kwargs)
        with open('logg.txt', 'a') as log:
            log.write(f'acction -- {funk.__name__}')
            nam = funk.__name__
        if nam == 'credit_to_card':
            print('aboba')
            with open('logg.txt', 'a') as log:
                log.write(f' number -- {BankAcount.Bancomat.nummm}  ')
                log.write(f'money -- {BankAcount.Bancomat.money}\n')
        if nam == 'withdraw':
            with open('logg.txt', 'a') as log:
                log.write(f' pin -- {BankAcount.Bancomat.pin}  ')
                log.write(f'money -- {BankAcount.Bancomat.money}')
        else:
            with open('logg.txt', 'a') as log:
                log.write(f' cvv -- {BankAcount.Bancomat.cvv}, date -- {BankAcount.Bancomat.date}, reciver -- {BankAcount.Bancomat.an_ac}\n')
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
    def print_money(self):
        return self.__money
    @loger
    @logger
    def credit_to_card(self, num, money):
        if num == None:
            return num
        if self.num == num:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @loger
    @logger
    def withdraw(self, pin, money):
        if self.__pin == pin:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @loger
    @logger
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
        @logger
        def credit_to_card(acount):
            try:
                num = int(input('input a number: '))
            except:
                return 'it is not number'
            try:
                money = int(input('number of money: '))
            except:
                return 'it is not number'
            BankAcount.Bancomat.nummm = num
            BankAcount.Bancomat.money = money
            return acount.credit_to_card(num, money)

        @staticmethod
        @logger
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
            BankAcount.Bancomat.pin = pin
            BankAcount.Bancomat.money = money * -1
            return acount.withdraw(pin, money)
        @staticmethod
        @logger
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
            BankAcount.Bancomat.money = money * -1
            BankAcount.Bancomat.cvv = cvv
            BankAcount.Bancomat.date = date
            BankAcount.Bancomat.an_ac = another_ack.ame
            acount.trans_to_card(another_ack, cvv, date, money)
            return 'transacttion complited'
ded = BankAcount('ded', 2283, 8753267899876535, 478)
vnuk = BankAcount('vnuk', 2285, 9753267899876535, 487)


print(ded._dat)
print(BankAcount.Bancomat.trans_to_card(ded, vnuk))
print(ded.print_money())
print(vnuk.print_money())
print(BankAcount.Bancomat.withdraw(ded))
print(ded.print_money())
print(BankAcount.Bancomat.credit_to_card(ded))
print(ded.print_money())

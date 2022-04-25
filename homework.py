import random
def square_num100k():
    for i in range(100000):
        s = i*i
        if s%2==0 and s!=0:
            with open('two.txt', 'a') as txt:
                txt.write(str(s)+ '\n')
        if s%3==0 and s!=0:
            with open('three.txt', 'a') as txt:
                txt.write(str(s)+ '\n')
        if s%5==0 and s!=0:
            with open('five.txt', 'a') as txt:
                txt.write(str(s)+ '\n')
        yield s


def gen_sawe_pass():
    pass1 = ''
    for i in range(7):
        letter = random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        pass1 += letter
    s = random.randint(100000, 999999)
    password = pass1 + str(s)
    yield password



def ret_save_pass():
    ansaf = ['qwertyu', 'iopasdf', 'ghjklzx', 'mnbvcxz', 'lkjhgfd', 'sapoiuy']
    ansafe = ['100000', '200000', '300000', '400000', '500000', '600000', '700000', '800000', '900000', '111111', '222222', '333333', '444444', '555555', '666666', '777777', '888888', '999999']
    passes = []
    while len(passes) != 1000:
        a = list(gen_sawe_pass())

        if a[0][0:7] not in ansaf:
            if a[0][7:18] not in ansafe:
                passes.append(a)
                yield a[0]




def gen(start=0, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if end < start and step > 0:
        return None

    if end > start and step < 0:
        return None

    if start != end:
        xc = end - start
        xc = xc // step
        if xc < 0:
            xc *= -1
        for i in range(xc+1):
            print(start)
            start += step




def gues():
    num = 999
    a =random.randint(0,100)
    while a != num:
        num = random.randint(0,100)
        yield num
    yield num, 'загадане число'


gen(1, -34, -3)
#print(list(gues()))
#print('------------------------')
#a = list(square_num100k())
#print('------------------------')
#print(list(ret_save_pass()))




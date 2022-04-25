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




def gen(start=0, end=1, step=1):
    list1 = []
    list2 = []
    list4 = []
    if start > end:
        start, end = end, start

        step *= -1
    while end != 0:
        list1.append(end)
        end -= 1
    while start != 0:
        list2.append(start)
        start -= 1
    list3 = list(set(list1) - set(list2))
    if step >= 2:
        s = len(list3)
        d = step - 1
        list4.append(list3.pop(d))
        while len(list4) != s // step:
            g = d + step - 1
            d=g
            list4.append(list3.pop(g))
        return list4
    if step == -1:
        while len(list3) != 0:
            list4.append(list3[-1])
            list3.pop(-1)
        return list4
    if step <= -2:
        s = len(list3)
        d = step
        list4.append(list3.pop(d))
        while len(list4) != s // (step * -1):
            g = d + step + 1
            d=g
            list4.append(list3.pop(g))
        return list4
    return list3

def gues():
    num = 999
    a =random.randint(0,100)
    while a != num:
        num = random.randint(0,100)
        yield num
    yield num, 'загадане число'


#print(list(gues()))
#print(gen(0, 10, step = -3))
#print(gen(10, 0 , step=-3))
#print('------------------------')
#a = list(square_num100k())
#print(a)
#print('------------------------')
#print(passwords)
#print('------------------------')
#print(list(ret_save_pass()))


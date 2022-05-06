def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umnozhit(a, b):
    return a * b
def podelit(a, b):
    return a / b
def podelit_celolochisleno(a, b):
    return a // b
def ostatok(a, b):
    return a % b
def stepen(a, b):
    return a ** b

def kalkulator(a, b, act):
    if act == '+':
        return plus(a, b)
    elif act == '-':
        return minus(a, b)
    elif act == '*':
        return umnozhit(a, b)
    elif act == '/':
        return podelit(a, b)
    elif act == '//':
        return podelit_celolochisleno(a, b)
    elif act == '%':
        return ostatok(a, b)
    elif act == '**':
        return stepen(a, b)
    else:
        return 'some error'
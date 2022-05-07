import validation
import kalkulator
def kalkulatorus(a, b, act):
    if act == '+':
        return kalkulator.plus(a, b)
    elif act == '-':
        return kalkulator.minus(a, b)
    elif act == '*':
        return kalkulator.umnozhit(a, b)
    elif act == '/':
        return kalkulator.podelit(a, b)
    elif act == '//':
        return kalkulator.podelit_celolochisleno(a, b)
    elif act == '%':
        return kalkulator.ostatok(a, b)
    elif act == '**':
        return kalkulator.stepen(a, b)
    else:
        return 'some error'
a = input("first number: ")
b = input("second number: ")
action = input("action: ")
if validation.is_operator(action) != False and validation.is_int(a) != False and validation.is_int(b) != False:
    a = validation.is_int(a)
    b = validation.is_int(b)
    print(kalkulatorus(a, b, action))
else:
    print('error')
    
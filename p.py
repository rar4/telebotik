import validation
import kalkulator
a = input("first number: ")
b = input("second number: ")
action = input("action: ")
if validation.is_operator(action) != False and validation.is_int(a) != False and validation.is_int(b) != False:
    a = validation.is_int(a)
    b = validation.is_int(b)
    print(kalkulator.kalkulator(a, b, action))
else:
    print('error')
    
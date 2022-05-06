import kalkulator
def is_int(a):
    try:
        a = int(a)
        return a
    except:
        return False
def is_operator(a):
    b = ['+', '-', '*', '/', '//', '%', '**']
    if a in b:
        return a
    else:
        return False


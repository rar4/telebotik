def timer(funk):
    import time
    def tim(*args, **kwargs):
        tim1 = time.time()
        time.sleep(1)
        result = funk(*args, **kwargs)
        tim2 = time.time()
        print(f'time of function is {tim2 - tim1} seconds')
        return  result
    return tim

@timer
def power(a = 1, b = 1):
    return a ** b

print(power(2, 3))

"""
def displayRange(lower,upper):
    while lower <= upper:
        print(lower)
        lower=lower +1
def displayRange(lower,upper):
    while lower <= upper:
        print(lower)
        displayRange(lower+ 1, upper)

def summation(lower,upper):
    if lower > upper:
        return 0
    else:
        return lower + summation(lower +1,upper)
    summation(5,15)
"""
def fib(n):
    if n <3:
        return 1
    else:
        return fib(n-1)+fib(n-2)
fib(8)
from decimal import getcontext, Decimal

getcontext().prec = 101
sqrt_2 = Decimal(2).sqrt()

def solution(s):
    _n = int(s)
    return str(summation(_n))

def summation(n):
    _np = int((sqrt_2-1)*n)
    if n == 0:
        return 0
    return n*_np + (n*(n+1))//2 - (_np*(_np+1))//2 - summation(_np)
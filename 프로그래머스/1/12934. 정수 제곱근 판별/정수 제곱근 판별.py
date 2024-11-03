def solution(n):
    x = n**(1/2)
    if x.is_integer():
        return (x+1)**2
    else:
        return -1
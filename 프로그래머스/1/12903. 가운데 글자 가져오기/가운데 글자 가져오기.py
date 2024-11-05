def solution(s):
    n = len(s)
    half = n // 2
    result = ''
    if n % 2 == 0:
        result += s[half-1]
        result += s[half]
    else:
        result += s[half]
    return result
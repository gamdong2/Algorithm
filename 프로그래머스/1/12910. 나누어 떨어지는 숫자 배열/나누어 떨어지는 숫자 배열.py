def solution(arr, divisor):
    a_list = []
    for a in arr:
        if a % divisor == 0:
            a_list.append(a)
    if len(a_list) == 0:
        a_list.append(-1)
    a_list.sort()
    return a_list
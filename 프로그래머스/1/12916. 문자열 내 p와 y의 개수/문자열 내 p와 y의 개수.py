def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    for i in s:
        if i in ('p', 'P'):
            count_p += 1
        elif i in ('y', 'Y'):
            count_y += 1
    if (count_p == 0) and (count_y == 0):
        return True
    elif count_p == count_y:
        return True
    else:
        return False
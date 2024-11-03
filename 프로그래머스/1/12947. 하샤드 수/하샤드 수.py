def solution(x):
    list_x = [int(i) for i in str(x)]
    sum_x = sum(list_x)
    if x % sum_x == 0:
        return True
    else:
        return False
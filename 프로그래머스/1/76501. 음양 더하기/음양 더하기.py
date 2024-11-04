def solution(absolutes, signs):
    total_num = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            total_num += absolute
        else:
            total_num -= absolute
    return total_num
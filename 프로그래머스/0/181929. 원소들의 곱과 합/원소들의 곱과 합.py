def solution(num_list):
    answer = 0
    add = 0
    mul = 1
    for num in num_list:
        add += num
        mul *= num
    if mul < add**2:
        answer = 1
    else:
        answer = 0
    return answer
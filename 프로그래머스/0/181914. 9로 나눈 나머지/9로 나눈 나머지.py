def solution(number):
    answer = 0
    num_sum = 0
    for num in number:
        num_sum += int(num)
    answer = num_sum % 9
    return answer
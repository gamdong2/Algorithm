def solution(numbers):
    numbers.sort()
    total_numbers = sum(range(0, 10))
    for i in numbers:
        total_numbers -= i   
    return total_numbers                      
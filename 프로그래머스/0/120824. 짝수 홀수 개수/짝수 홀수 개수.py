def solution(num_list):
    even_count = 0
    odd_count = 0
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return [even_count, odd_count]

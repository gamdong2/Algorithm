def solution(n):
    count = 0
    for start in range(1, n + 1):
        sum_value = 0
        for num in range(start, n + 1):
            sum_value += num
            if sum_value == n:
                count += 1
                break
            elif sum_value > n:
                break
    return count

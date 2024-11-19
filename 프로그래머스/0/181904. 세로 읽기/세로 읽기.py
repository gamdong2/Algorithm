def solution(my_string, m, c):
    result = []
    for i in range(len(my_string)):
        if i % m == c - 1:
            result.append(my_string[i])
    return ''.join(result)

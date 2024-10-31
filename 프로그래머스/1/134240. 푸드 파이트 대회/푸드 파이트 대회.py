def solution(food):
    answer = ''

    for i in range(1, len(food)):
        count = food[i] // 2
        answer += str(i) * count

    result = answer + '0' + answer[::-1]
    return result

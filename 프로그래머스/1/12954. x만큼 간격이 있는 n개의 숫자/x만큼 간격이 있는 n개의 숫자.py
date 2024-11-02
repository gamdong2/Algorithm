def solution(x, n):
    answer = []
    new = x
    for i in range(n):
        answer.append(new)
        new += x
    return answer
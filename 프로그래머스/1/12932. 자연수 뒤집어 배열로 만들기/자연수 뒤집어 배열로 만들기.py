def solution(n):
    answer = []
    n_str = str(n)
    n_str = str(n)[::-1]
    for i in n_str:
        answer.append(int(i))
    return answer
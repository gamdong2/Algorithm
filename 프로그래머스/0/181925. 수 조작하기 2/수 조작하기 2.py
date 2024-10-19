def solution(numLog):
    answer = ''
    n = len(numLog)
    for i in range(n-1):
        diff = numLog[i+1] - numLog[i]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    return answer
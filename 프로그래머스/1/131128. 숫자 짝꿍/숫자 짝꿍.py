from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    result = []
    for num in range(9, -1, -1):
        str_num = str(num)
        if str_num in count_X and str_num in count_Y:
            result.append(str_num * min(count_X[str_num], count_Y[str_num]))
    
    answer = ''.join(result)
    
    if not answer:
        return '-1'
    if answer == '0' * len(answer):
        return '0'
    
    return answer

def solution(my_string, overwrite_string, s):
    answer = ''
    n = len(overwrite_string)    
    for i in range(len(my_string)):
        if i >= s and i < s + n: 
            answer += overwrite_string[i - s] 
        else:
            answer += my_string[i]      
    return answer

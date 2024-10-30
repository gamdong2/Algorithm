def solution(t, p):
    answer = 0
    p_length = len(p)
    p_value = int(p)
    
    for i in range(len(t) - p_length + 1):
        substring = t[i:i + p_length] 
        t_value = int(substring)  
        
        if t_value <= p_value:
            answer += 1
            
    return answer
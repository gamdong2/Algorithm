def solution(n, m, section):
    answer = 0  
    current_pos = 0  

    for s in section:
        if s >= current_pos:
            answer += 1
            current_pos = s + m

    return answer

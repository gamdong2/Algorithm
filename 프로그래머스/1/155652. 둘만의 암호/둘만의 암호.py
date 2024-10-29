def solution(s, skip, index):

    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    answer = ''

    for char in s:
        current_pos = alphabet.index(char) 
        new_pos = (current_pos + index) % len(alphabet)  
        answer += alphabet[new_pos]
    return answer

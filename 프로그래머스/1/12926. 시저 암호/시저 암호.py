def solution(s, n):
    result = []
    for char in s:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char.isupper():  
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else: 
            result.append(char)
    return ''.join(result)

s = "AB z"
n = 1
print(solution(s, n))

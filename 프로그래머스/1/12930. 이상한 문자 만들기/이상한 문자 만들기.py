def solution(s):
    result = []
    s_list = s.split(" ")
    
    for word in s_list:
        transformed_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                transformed_word += char.upper()
            else:
                transformed_word += char.lower()
        result.append(transformed_word)
    
    return ' '.join(result)
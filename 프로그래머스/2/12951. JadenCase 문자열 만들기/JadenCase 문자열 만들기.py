def solution(s):

    words = s.split(" ")
    jaden_case_words = [
        word.capitalize() if word else "" 
        for word in words
    ]

    return " ".join(jaden_case_words)
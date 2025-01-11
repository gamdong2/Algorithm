def solution(myString):
    result = ''.join('l' if char < 'l' else char for char in myString)
    return result

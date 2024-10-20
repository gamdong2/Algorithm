def solution(l, r):
    answer = []
    
    # l부터 r까지의 범위에서 숫자를 하나씩 확인
    for num in range(l, r+1):
        # num의 각 자리 숫자가 '0' 또는 '5'로만 이루어졌는지 확인
        if all(char in '05' for char in str(num)):
            answer.append(num)
    
    # answer 리스트가 비어있으면 -1을 추가
    if not answer:
        answer.append(-1)
    
    return answer

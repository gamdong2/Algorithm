def solution(n):
    list_n = [int(i) for i in str(n)]
    list_n.sort(reverse = True)
    return int(''.join(map(str, list_n)))
                  
    
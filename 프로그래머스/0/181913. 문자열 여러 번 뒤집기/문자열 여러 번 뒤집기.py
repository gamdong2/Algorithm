def solution(my_string, queries):
    answer = ''
    my_list = list(my_string)
    for s, e in queries:
        my_list[s:e+1] = my_list[s:e+1][::-1]
    answer = ''.join(my_list) 
    return answer
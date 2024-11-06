def solution(my_string, s, e):
    str_list = list(my_string)
    str_list[s:e+1] = str_list[s:e+1][::-1]
    return ''.join(str_list)

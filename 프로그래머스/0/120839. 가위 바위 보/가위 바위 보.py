def solution(rsp):
    win_map = {'2': '0', '0': '5', '5': '2'}
    return ''.join(win_map[char] for char in rsp)

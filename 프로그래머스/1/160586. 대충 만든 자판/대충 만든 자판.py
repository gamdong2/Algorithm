def solution(keymap, targets):
    min_keypress = {}
    for i, keys in enumerate(keymap):
        for j, char in enumerate(keys):
        
            if char in min_keypress:
                min_keypress[char] = min(min_keypress[char], j + 1)
            else:
                min_keypress[char] = j + 1
    answer = []
    for target in targets:
        total_presses = 0
        for char in target:
            if char not in min_keypress:
                total_presses = -1
                break
            total_presses += min_keypress[char]
        answer.append(total_presses)
    
    return answer

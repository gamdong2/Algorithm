def solution(babbling):
    answer = 0
    valid_sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        temp = word
        for sound in valid_sounds:
            if sound * 2 not in temp:
                temp = temp.replace(sound, ' ')
        if temp.strip() == '':
            answer += 1

    return answer

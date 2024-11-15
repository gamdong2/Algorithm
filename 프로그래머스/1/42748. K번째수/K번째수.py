def solution(array, commands):
    result = []
    # commands = [[i, j, k], [i, j, k], [i, j, k]]
    for command in commands:
        i, j, k = command
        new_array = array[i-1:j]
        new_array.sort()
        result.append(new_array[k-1])
    return result
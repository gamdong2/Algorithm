def solution(s):
    transformation_count = 0
    removed_zeros_count = 0

    while s != "1":
        removed_zeros_count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        transformation_count += 1

    return [transformation_count, removed_zeros_count]

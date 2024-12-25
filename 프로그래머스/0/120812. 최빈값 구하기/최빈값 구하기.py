from collections import Counter

def solution(array):
    counts = Counter(array)
    most_common = counts.most_common()
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]

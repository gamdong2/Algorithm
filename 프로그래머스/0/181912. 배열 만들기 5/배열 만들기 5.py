def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        subStrs = i[s:s+l]
        if int(subStrs) > k:
            answer.append(int(subStrs))
    return answer
def solution(numbers):
    result = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    return sorted(result)

numbers = [2, 1, 3, 4, 1]
result = solution(numbers)
print(result)

def solution(numer1, denom1, numer2, denom2):
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    common_divisor = find_gcd(numerator, denominator)
    answer = [numerator // common_divisor, denominator // common_divisor]
    return answer

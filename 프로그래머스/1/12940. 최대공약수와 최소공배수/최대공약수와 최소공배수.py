def solution(a, b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
            break
    lcm_value = (a * b) // gcd_value
    return [gcd_value, lcm_value]
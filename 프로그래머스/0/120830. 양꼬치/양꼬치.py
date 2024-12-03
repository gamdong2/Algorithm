def solution(n, k):
    service_drinks = n // 10
    total_cost = (n * 12000) + ((k - service_drinks) * 2000)
    return total_cost

def solution(price, money, count):
    for i in range(count):
        final_price += price * i
    final_money = money - final_price
    if final_money >= final_price:
        lack = 0
    else:
        lack = final_price
    return lack

def solution(price, money, count):
    # 총 비용 계산
    total_cost = price * count * (count + 1) // 2
    # 부족한 금액 계산
    lack = total_cost - money
    # 부족한 금액이 음수일 경우 0으로 반환
    return max(0, lack)

       
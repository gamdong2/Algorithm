import datetime

def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    date = datetime.date(2016, a, b)
    day_of_week = date.weekday()
    return days[(day_of_week + 1) % 7]

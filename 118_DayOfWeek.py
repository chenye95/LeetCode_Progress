from datetime import datetime
from calendar import day_name

def dayOfTheWeek(day: int, month: int, year: int) -> str:
    return day_name[datetime(year, month, day).weekday()]

print(dayOfTheWeek(year=2020, month=1, day=26))

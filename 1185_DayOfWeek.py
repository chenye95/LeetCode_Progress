"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
"Saturday"}.
"""
from calendar import day_name
from datetime import datetime


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    return day_name[datetime(year, month, day).weekday()]


assert dayOfTheWeek(year=2020, month=1, day=26) == 'Sunday'

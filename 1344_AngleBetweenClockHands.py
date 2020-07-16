"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""


def angle_clock(hour: int, minutes: int) -> float:
    """
    :param hour: 1 <= hour <= 12
    :param minutes: 0 <= minutes <= 59
    :return: the smaller angle (in degrees) formed between the hour and the minute hand
    """
    minute_angle = 6 * minutes
    hour = hour if hour < 12 else 0
    hour_angle = 30 * hour + 0.5 * minutes
    angle_difference = abs(hour_angle - minute_angle)
    return angle_difference if angle_difference <= 180 else 360 - angle_difference


assert angle_clock(hour=12, minutes=30) == 165
assert angle_clock(hour=3, minutes=30) == 75
assert angle_clock(hour=3, minutes=15) == 7.5
assert angle_clock(hour=4, minutes=50) == 155
assert angle_clock(hour=12, minutes=0) == 0
assert angle_clock(hour=1, minutes=57) == 76.5

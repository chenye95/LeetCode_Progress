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


test_cases = [(12, 30, 165), (3, 30, 75), (3, 15, 7.5), (4, 50, 155), (12, 0, 0), (1, 57, 76.5), ]
for test_hour, test_minutes, expected_angle in test_cases:
    assert angle_clock(test_hour, test_minutes) == expected_angle

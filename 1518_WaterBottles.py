"""
Given initial_bottles full water bottles, you can exchange num_exchange empty water bottles for one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Return the maximum number of water bottles you can drink.
"""


def num_water_bottles(initial_bottles: int, num_exchange: int) -> int:
    """
    Simulation
    :param initial_bottles: num_bottles full bottles to start with
    :param num_exchange: change num_exchange empty bottles for 1 full bottle
    :return: total number of bottles consumed in the end
    """
    full_count = initial_bottles
    total_count = empty_count = 0
    while full_count > 0 or empty_count >= num_exchange:
        total_count += full_count
        empty_count += full_count
        full_count, empty_count = empty_count // num_exchange, empty_count % num_exchange
    return total_count


test_cases = [(9, 3, 13), (15, 4, 19), (5, 5, 6), (2, 3, 2), ]
for test_initial, test_exchange, expected_output in test_cases:
    assert num_water_bottles(test_initial, test_exchange) == expected_output, expected_output

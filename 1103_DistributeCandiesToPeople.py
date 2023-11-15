"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last
person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person,
and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the
end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
"""
from typing import List


def distribute_candies(candies: int, num_people: int) -> List[int]:
    """
    :param candies: total candies to be distributed
    :param num_people: no of people sharing candies
    :return: no. of candies each person gets
    """
    round_no = 0
    current_round_total = (num_people + 1) * num_people // 2  # sum(range(1, num_people + 1))
    while candies >= current_round_total:
        round_no += 1
        candies -= current_round_total
        current_round_total += num_people * num_people

    shared_addition = (round_no - 1) * round_no // 2 * num_people  # sum(range(round_no)) * num_people
    candy_distribution = [shared_addition + i * round_no for i in range(1, num_people + 1)]

    next_person, next_candy_batch = 0, round_no * num_people + 1
    while candies >= next_candy_batch:
        candy_distribution[next_person] += next_candy_batch
        candies -= next_candy_batch
        next_person += 1
        next_candy_batch += 1
    candy_distribution[next_person] += candies

    return candy_distribution


test_cases = [
    (7, 4, [1, 2, 3, 1]),
    (10, 3, [5, 2, 3]),
]
for test_c, test_n, expected_value in test_cases:
    assert distribute_candies(candies=test_c, num_people=test_n) == expected_value

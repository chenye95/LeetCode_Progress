"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives
east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th
trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The
locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.
"""
from typing import List


def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    """
    :param trips: trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip
    :param capacity: empty seats initially available for passengers
    :return: whether it can pick up and drop off all passengers for all the given trips.
    """
    # Play through time to pick up and drop off passengers
    for _, n_count in sorted(x for n_passenger, t_start, t_end in trips
                             for x in [(t_start, n_passenger), (t_end, -n_passenger)]):
        capacity -= n_count
        if capacity < 0:
            return False
    return True


assert car_pooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4) is False
assert car_pooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5) is True
assert car_pooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3) is True
assert car_pooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11) is True

"""
Implement the class UndergroundSystem that supports three methods:

1. checkIn(int customer_id, string station_name, int t)
- A customer with customer_id card equal to customer_id, gets in the station station_name at time t.
- A customer can only be checked into one place at a time.

2. checkOut(int customer_id, string station_name, int t)
- A customer with customer_id card equal to customer_id, gets out from the station station_name at time t.

3. getAverageTime(string start_station, string end_station)

Returns the average time to travel between the start_station and the end_station.
The average time is computed from all the previous traveling from start_station to end_station that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at
some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
"""
from collections import defaultdict
from typing import DefaultDict, Dict, Tuple


class UndergroundSystem:
    def __init__(self):
        # customer_id -> (start_station, check_in_time)
        self.outstanding_trip: Dict[int, Tuple[str, int]] = dict()
        # (start_station, end_station) -> (total_duration, trip_count)
        self.completed_trip: DefaultDict[Tuple[str, str], Tuple[int, int]] = defaultdict(lambda: (0, 0))

    def check_in(self, customer_id: int, station_name: str, t: int) -> None:
        """
        customer_id checks in at station_name at time t
        """
        self.outstanding_trip[customer_id] = (station_name, t)

    def check_out(self, customer_id: int, station_name: str, t: int) -> None:
        """
        customer_id checks out at station_name at time t
        """
        start_station, start_time = self.outstanding_trip[customer_id]
        trip_key = (start_station, station_name)
        old_time, old_count = self.completed_trip[trip_key]
        self.completed_trip[trip_key] = (old_time + t - start_time, old_count + 1)

    def get_average_time(self, start_station: str, end_station: str) -> float:
        """
        :return: return average travel time from start_station to end_station among completed, direct trips
        """
        total_time, total_count = self.completed_trip[(start_station, end_station)]
        return float(total_time) / total_count


undergroundSystem = UndergroundSystem()
undergroundSystem.check_in(45, "Leyton", 3)
undergroundSystem.check_in(32, "Paradise", 8)
undergroundSystem.check_in(27, "Leyton", 10)
undergroundSystem.check_out(45, "Waterloo", 15)
undergroundSystem.check_out(27, "Waterloo", 20)
undergroundSystem.check_out(32, "Cambridge", 22)
assert undergroundSystem.get_average_time("Paradise", "Cambridge") == 14
# There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
assert undergroundSystem.get_average_time("Leyton", "Waterloo") == 11
# There were two travels from "Leyton" to "Waterloo", a customer with customer_id=45 from time=3 to time=15 and a
# customer with customer_id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.check_in(10, "Leyton", 24)
assert undergroundSystem.get_average_time("Leyton", "Waterloo") == 11
undergroundSystem.check_out(10, "Waterloo", 38)
assert undergroundSystem.get_average_time("Leyton", "Waterloo") == 12

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

ote:
1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.
4. One must use all the tickets once and only once.
"""
from collections import defaultdict
from typing import List, Tuple


def find_itinerary(tickets: List[Tuple[str, str]]) -> List[str]:
    """
    Greedy algorithm, try in alphabetic order

    :param tickets: list of airline tickets, by pairs of (departure, arrival) airports
    :return: itinerary for the person who departs from JFK; return smallest lexical order if multiple valid ones exist
    """
    connection_map = defaultdict(list)
    # reversed lexical order
    for from_city, to_city in sorted(tickets, reverse=True):
        connection_map[from_city] += [to_city]

    reversed_route, stack = [], ['JFK']
    while stack:
        while connection_map[stack[-1]]:
            stack.append(connection_map[stack[-1]].pop()),
        reversed_route.append(stack.pop())
    return reversed_route[::-1]


test_cases = [([("ATL", "BOS"), ("BOS", "ZRH"), ("JFK", "ATL"), ("ZRH", "BOS"), ("BOS", "JFK")],
               ["JFK", "ATL", "BOS", "ZRH", "BOS", "JFK"]),
              ([("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")],
               ["JFK", "MUC", "LHR", "SFO", "SJC"]),
              ([("JFK", "SFO"), ("JFK", "ATL"), ("SFO", "ATL"), ("ATL", "JFK"), ("ATL", "SFO")],
               ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
              ([("JFK", "ATL"), ("JFK", "SFO"), ("SFO", "JFK"), ("JFK", "MUC"), ("MUC", "JFK")],
               ["JFK", "MUC", "JFK", "SFO", "JFK", "ATL"]),
              ([("JFK", "ATL"), ("JFK", "SFO"), ("SFO", "JFK"), ("JFK", "MUC"), ("MUC", "JFK"), ("ATL", "JFK")],
               ["JFK", "ATL", "JFK", "MUC", "JFK", "SFO", "JFK"]),
              ]
for input_tickets, expected_output in test_cases:
    assert find_itinerary(input_tickets) == expected_output

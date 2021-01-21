"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can
return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and
cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245",
"192.168.1.312" and "192.168@1.1" are invalid IP addresses.
"""
from typing import List


def restore_ip_address(s: str) -> List[str]:
    def dfs_helper(remainder: str, part_idx: int, path_so_far: str, ref_result: List[str]) -> None:
        if part_idx == 4:
            if not remainder:
                # Remove trailing .
                ref_result.append(path_so_far[:-1])
            return
        # Each part can not be longer than 3 digits
        if not remainder or 3 * (4 - part_idx) < len(remainder):
            return

        # Single Digit
        dfs_helper(remainder[1:], part_idx + 1, path_so_far + remainder[0] + '.', ref_result)
        # Two or Three Digits, need to avoid leading 0
        if remainder[0] != '0' and len(remainder) >= 2:
            dfs_helper(remainder[2:], part_idx + 1, path_so_far + remainder[:2] + '.', ref_result)
            if len(remainder) >= 3 and remainder[:3] < '256':
                dfs_helper(remainder[3:], part_idx + 1, path_so_far + remainder[:3] + '.', ref_result)

    return_list = []
    dfs_helper(s, 0, "", return_list)
    return return_list


test_cases = [("25525511135", ["255.255.11.135", "255.255.111.35"]),
              ("0000", ["0.0.0.0"]),
              ("1111", ["1.1.1.1"])]
for s, expected_output in test_cases:
    assert set(restore_ip_address(s)) == set(expected_output)

"""
Given a string IP. We need to check If IP is a valid IPv4 address, valid IPv6 address or not a valid IP address. Return
 "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a valid IP of any
 type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", "192.168.1.00" and
"192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
- 1 <= xi.length <= 4
- xi is hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and/or upper-case English
 letters ('A' to 'F').
- Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses
but "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""


def valid_ip_address(ip_address: str) -> str:
    """
    :param ip_address: ip_address to verify
    :return: "IPv4" or "IPv6" or "Neither"
    """
    ip_v4_split = ip_address.split('.')
    if len(ip_v4_split) == 4:
        if all([part_i and part_i.isdigit() and
                (1 <= int(part_i) <= 255 and part_i[0] != '0' or part_i == '0') for part_i in ip_v4_split]):
            return "IPv4"

    ip_v6_split = ip_address.split(':')
    v6_set = {'0', '1', '2', '3', '4', '5',
              '6', '7', '8', '9',
              'a', 'b', 'c', 'd', 'e', 'f',
              'A', 'B', 'C', 'D', 'E', 'F', }
    if len(ip_v6_split) == 8:
        if all([1 <= len(part_i) <= 4 and set(part_i) <= v6_set for part_i in ip_v6_split]):
            return "IPv6"

    return "Neither"


test_cases = [("192.168.1.1", "IPv4"),
              ("192.168.1.0", "IPv4"),
              ("192.168.01.1", "Neither"),
              ("192.168.1.00", "Neither"),
              ("192.168@1.1", "Neither"),
              ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
              ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
              ("2001:0db8:85a3::8A2E:037j:7334", "Neither"),
              ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", "Neither"),
              ("2001:0dg8:85a3:0000:0000:8a2e:0370:7334", "Neither"),
              ("2001:0de8:85Z3:0000:0000:8a2e:0370:7334", "Neither"), ]
for test_ip_address, expected_output in test_cases:
    assert valid_ip_address(test_ip_address) == expected_output, test_ip_address

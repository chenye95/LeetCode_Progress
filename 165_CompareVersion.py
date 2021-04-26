"""
Compare two version numbers version_1 and version_2.
If version_1 > version_2 return 1; if version_1 < version_2 return -1;otherwise return 0.
"""


def compare_version(version_1: str, version_2: str) -> int:
    """
    :return: 1 if version_1 > version_2, -1 if version_1 < version_2 return -1, 0 otherwise
    """
    version1_str = version_1.split('.')
    version2_str = version_2.split('.')

    for version1_i, version2_i in zip(version1_str, version2_str):
        version1_i_int = int(version1_i)
        version2_i_int = int(version2_i)
        if version1_i_int > version2_i_int:
            return 1
        elif version1_i_int < version2_i_int:
            return -1

    if len(version1_str) == len(version2_str):
        return 0
    elif len(version1_str) > len(version2_str):
        remainder_str, return_val = version1_str[len(version2_str):], 1
    else:
        remainder_str, return_val = version2_str[len(version1_str):], -1

    for c_i in remainder_str:
        if int(c_i) > 0:
            return return_val

    return 0


test_cases = [("1", "1.1", -1),
              ('0.1', '1.1', -1),
              ('1.0.1', '1', 1),
              ("7.5.2.4", "7.5.3", -1),
              ("1.01", "1.001", 0),
              ("0.9.9.9.9.9.9.9.9.9.9.9.9", "1.0", -1),
              ("1.0", "1.0.0", 0),
              ("1.0", "1.0.0.0.0.1", -1), ]
for test_version_1, test_version_2, expected_outcome in test_cases:
    assert compare_version(version_1=test_version_1, version_2=test_version_2) == expected_outcome

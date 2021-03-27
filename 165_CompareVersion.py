"""
Compare two version numbers version_1 and version_2.
If version_1 > version_2 return 1; if version_1 < version_2 return -1;otherwise return 0.
"""


def compare_version(version_1: str, version_2: str) -> int:
    """
    :return: 1 if version_1 > version_2, -1 if version_1 < version_2 return -1, 0 otherwise
    """
    version1_int = [int(segment) for segment in version_1.split('.')]
    version2_int = [int(segment) for segment in version_2.split('.')]
    if len(version1_int) < len(version2_int):
        version1_int.extend([0] * (len(version2_int) - len(version1_int)))
    elif len(version1_int) > len(version2_int):
        version2_int.extend([0] * (len(version1_int) - len(version2_int)))

    for i in range(len(version1_int)):
        if version1_int[i] < version2_int[i]:
            return -1
        elif version1_int[i] > version2_int[i]:
            return 1
    return 0


test_cases = [('0.1', '1.1', -1),
              ('1.0.1', '1', 1),
              ("7.5.2.4", "7.5.3", -1),
              ("1.01", "1.001", 0), ]
for test_version_1, test_version_2, expected_outcome in test_cases:
    assert compare_version(version_1=test_version_1, version_2=test_version_2) == expected_outcome

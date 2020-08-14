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

    i = 0
    while i < len(version1_int):
        if version1_int[i] < version2_int[i]:
            return -1
        elif version1_int[i] > version2_int[i]:
            return 1
        i += 1
    return 0


assert compare_version(version_1='0.1', version_2='1.1') == -1
assert compare_version(version_1='1.0.1', version_2='1') == 1
assert compare_version(version_1="7.5.2.4", version_2="7.5.3") == -1
assert compare_version(version_1="1.01", version_2="1.001") == 0

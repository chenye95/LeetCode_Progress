"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
"""
def compareVersion(version1: str, version2: str) -> int:
    version1_int = [int(segment) for segment in version1.split('.')]
    version2_int = [int(segment) for segment in version2.split('.')]
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

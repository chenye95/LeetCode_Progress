"""
Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute,
you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a
suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name
remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when
you create it.
"""
from typing import List


def get_folder_names(names: List[str]) -> List[str]:
    """
    :param names: length n such that you attempt to create a folder with the name names[i]
    :return: length n where return_list[i] is the actual name the system will assign to the ith folder
    """
    seen, k_value = set(), dict()
    return_list = [""] * len(names)
    for i, name in enumerate(names):
        k = k_value.get(name, 0)
        unique_name = name
        while unique_name in seen:
            k += 1
            unique_name = name + '(' + str(k) + ')'
        k_value[name] = k
        return_list[i] = unique_name
        seen.add(unique_name)
    return return_list


assert get_folder_names(["wano", "wano", "wano", "wano"]) == ["wano", "wano(1)", "wano(2)", "wano(3)"]
assert get_folder_names(["pes", "fifa", "gta", "pes(2019)"]) == ["pes", "fifa", "gta", "pes(2019)"]
assert get_folder_names(["gta", "gta(1)", "gta", "avalon"]) == ["gta", "gta(1)", "gta(2)", "avalon"]
assert get_folder_names(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]) == \
       ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"]

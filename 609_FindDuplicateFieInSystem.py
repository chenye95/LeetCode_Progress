"""
Given a list paths of directory info, including the directory path, and all the files with contents in this directory,
 return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:
    - "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively
 in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root
 directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that
 have the same content. A file path is a string that has the following format:
    - "directory_path/file_name.txt"
"""
from collections import defaultdict
from typing import List


def find_duplicate(paths: List[str]) -> List[List[str]]:
    """
    :param paths: list of "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
    :return: list of groups of duplicate file paths [["directory_path/file_name.txt"]]
    """
    content_file_path = defaultdict(list)
    for folder_str in paths:
        files_list = folder_str.split(' ')
        folder_path = files_list[0] + '/'
        for file_name_content in files_list[1:]:
            file_name, file_content = file_name_content.split('(')
            content_file_path[file_content].append(folder_path + file_name)
    return [content_path_list for content_path_list in content_file_path.values() if len(content_path_list) > 1]


test_cases = [(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
               [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]),
              (["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"],
               [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]),
              (["root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)", "root/c/d 4.txt(efggdfh)"], []),
              (["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
               [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]), ]
for test_paths, expected_list in test_cases:
    got_list = find_duplicate(test_paths)
    got_list = sorted(sorted(list_i) for list_i in got_list)
    expected_list = sorted(sorted(list_i) for list_i in expected_list)
    assert got_list == expected_list

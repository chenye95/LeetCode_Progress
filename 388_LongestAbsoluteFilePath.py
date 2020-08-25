"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
    dir
        subdir1
        subdir2
            file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.
"""


def longest_absolute_path(input: str) -> int:
    """
    :param input: string representation of folder structures, level 1
    :return: longest absolute path
    """
    max_len = 0
    # 'dir' is level 0
    # path_len_by_level[level_i + 1] total length til level_i sub folder
    path_len_by_level = {0: 0}
    for line in input.splitlines():
        folder_file_name = line.lstrip('\t')
        level_i = len(line) - len(folder_file_name)
        if '.' in folder_file_name:
            # line represents a file name
            max_len = max(max_len, path_len_by_level[level_i] + len(folder_file_name))
        else:
            # line represents a level_i folder name
            path_len_by_level[level_i + 1] = path_len_by_level[level_i] + len(folder_file_name) + 1

    return max_len


test_cases = [("dir/subdir2/subsubdir2/", 0),
              ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", 32),
              ("dir\n\ta\n\t\taa\n\t\t\taaa\n\t\t\t\tfile1.txt\n\taaaaaaaaaaaaaaaaaaaaa\n\t\tsth.png", 33), ]
for test_input, expected_output in test_cases:
    assert longest_absolute_path(test_input) == expected_output, test_input

"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file
system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory
up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any
other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no
    period '.' or double period '..')

Return the simplified canonical path.
"""


def simplify_path(path: str) -> str:
    path_stack = []
    components = [c_i for c_i in path.split('/') if c_i]
    for c_i in components:
        if c_i == '.':
            continue
        elif c_i == '..':
            if path_stack:
                path_stack.pop()
        else:
            path_stack.append(c_i)
    return '/' + '/'.join(path_stack)


test_cases = [("/../", "/"),
              ("/home//foo/", "/home/foo"),
              ("/a/./b/../../c/", "/c"),
              ("/home/", "/home")]
for test_path, expected_output in test_cases:
    assert simplify_path(test_path) == expected_output

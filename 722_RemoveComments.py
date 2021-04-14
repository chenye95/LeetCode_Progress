"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the
source code. This represents the result of splitting the original source code string by the newline character \n.
"""
from typing import List


def remove_comments(source: List[str]) -> List[str]:
    """
    :param source: an array where source[i] is the i-th line of the C++ source code. This represents the result of
    splitting the original source code string by the newline character \n.
    :return: After removing the comments from the C++ source code, return the C++ source code in the same format
    """
    return_list = []
    inside_block, new_line = False, None
    for line_i in source:
        position_j = 0
        if not inside_block:
            new_line = []
        while position_j < len(line_i):
            if line_i[position_j:position_j + 2] == '/*' and not inside_block:
                # Start of block comment, continue with current line to handle one line block comment
                inside_block = True
                position_j += 1
            elif line_i[position_j:position_j + 2] == '*/' and inside_block:
                # End of block comment, continue with current line to handle one line block comment
                inside_block = False
                position_j += 1
            elif not inside_block and line_i[position_j:position_j + 2] == '//':
                # Inline comment, skip remainder of line_i
                break
            elif not inside_block:
                new_line.append(line_i[position_j])
            position_j += 1
        if new_line and not inside_block:
            return_list.append(''.join(new_line))

    return return_list


test_cases = [
    (["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
      "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"],
     ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]),
    (["a/*comment", "line", "more_comment*/b"], ["ab"]),
    (["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"],
     ['struct Node{', '    ', '    int size;', '    int val;', '};']),
]
for input_source, output_string in test_cases:
    assert remove_comments(input_source) == output_string

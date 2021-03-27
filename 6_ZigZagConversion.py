"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows of like this:
(you may want to display this pattern in a fixed font for better legibility)
And then read line by line: "PAHNAPLSIIGYIR"
"""


def convert_calculate(s: str, num_rows: int) -> str:
    """
    :param num_rows: number of rows used in zig zag pattern
    :return: s written in zig-zag pattern and read horizontally
    """
    if not s or len(s) <= 1 or num_rows == 1:
        return s
    repetition_group = 2 * (num_rows - 1)
    group_count = (len(s) + repetition_group - 1) // repetition_group

    return_result = []
    for row_i in range(num_rows):
        if row_i == 0 or row_i == num_rows - 1:
            row_i_list = [s[repetition_group * i + row_i] for i in range(group_count - 1)]
            if (group_count - 1) * repetition_group + row_i < len(s):
                row_i_list.append(s[repetition_group * (group_count - 1) + row_i])
            return_result.append(''.join(row_i_list))
        else:
            row_i_list = [s[repetition_group * i + row_i] + s[repetition_group * (i + 1) - row_i]
                          for i in range(group_count - 1)]
            if (group_count - 1) * repetition_group + row_i < len(s):
                row_i_list.append(s[repetition_group * (group_count - 1) + row_i])
                if group_count * repetition_group - row_i < len(s):
                    row_i_list.append(s[group_count * repetition_group - row_i])
            return_result.append(''.join(row_i_list))

    return ''.join(return_result)


def convert_simulate(s: str, num_rows: int) -> str:
    if num_rows == 1 or not s or len(s) <= 1:
        return s

    rows_list = [""] * num_rows
    row_index = 0
    going_down = True

    for ch in s:
        rows_list[row_index] += ch
        if row_index == num_rows - 1:
            going_down = False
        elif row_index == 0:
            going_down = True

        if going_down:
            row_index += 1
        else:
            row_index -= 1

    return ''.join(rows_list)


test_cases = [("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
              ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
              ("A", 1, "A"),
              ("AB", 1, "AB"),
              ("A", 2, "A"), ]
for convert in [convert_simulate, convert_calculate]:
    for test_s, test_rows, expected_output in test_cases:
        assert convert(s=test_s, num_rows=test_rows) == expected_output, convert.__name__

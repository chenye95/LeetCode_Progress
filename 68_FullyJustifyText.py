"""
Given an array of words and a width max_width, format the text such that each line has exactly max_width characters
and is fully (left and right) justified.
"""
from typing import List


def fully_justify(words: List[str], max_width: int) -> List[str]:
    """
    :param words: array of words to be fully justified
    :param max_width: max_width for each line
    :return: list of strings representing fully justified rendering of words
    """
    scanner = 0
    output_lines = []
    current_line_start = 0
    current_line_len = 0
    current_line_count = 0
    current_blank_count = -1
    while scanner < len(words):
        if current_line_len + len(words[scanner]) + current_blank_count + 1 <= max_width:  # have room for next word
            current_line_len += len(words[scanner])
            current_blank_count += 1
            current_line_count += 1
            scanner += 1
        else:  # construct current line
            if current_line_count > 1:
                current_line = ""
                diff = max_width - current_line_len
                quotient, remainder = divmod(diff, (current_line_count - 1))
                for j in range(current_line_start, current_line_start + current_line_count - 1):
                    current_line += words[j] + ' ' * (quotient + (remainder > j - current_line_start))
                current_line += words[current_line_start + current_line_count - 1]
            else:
                current_line = words[current_line_start]
                current_line += ' ' * (max_width - len(current_line))
            output_lines.append(current_line)
            # Reset for Next Line
            current_line_start = scanner
            current_line_count = 0
            current_line_len = 0
            current_blank_count = -1
    # Last Line
    if current_line_count > 0:  # still processing last line
        current_line = ' '.join(words[current_line_start:])
    else:  # last line processed, need to re-justify
        current_line = ' '.join(output_lines[-1].split())
    current_line += ' ' * (max_width - len(current_line))
    output_lines.append(current_line)
    return output_lines


test_cases = [(["This", "is", "an", "example", "of", "text", "justification.", ], 16,
               ["This    is    an",
                "example  of text",
                "justification.  ", ]),
              (["What", "must", "be", "acknowledgment", "shall", "be"], 16,
               ["What   must   be",
                "acknowledgment  ",
                "shall be        ", ]),
              (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
                "Art", "is", "everything", "else", "we", "do"], 20,
               ["Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ", ]), ]
for test_words, test_width, expected_output in test_cases:
    assert fully_justify(words=test_words, max_width=test_width) == expected_output

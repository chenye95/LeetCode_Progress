"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.
"""
from __future__ import annotations
from typing import List, Any

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    scanner = 0
    output_lines = []
    current_line_start = 0
    current_line_len = 0
    current_line_count = 0
    current_blk_count = -1
    while scanner < len(words):
        if current_line_len + len(words[scanner]) + current_blk_count + 1 <= maxWidth: # have room for next word
            current_line_len += len(words[scanner])
            current_blk_count += 1
            current_line_count += 1
            scanner += 1
        else: # construct current line
            if current_line_count > 1:
                current_line = ""
                diff = maxWidth - current_line_len
                quotient, remainder = divmod(diff, (current_line_count - 1))
                for j in range(current_line_start, current_line_start + current_line_count - 1):
                    current_line += words[j] + ' ' * (quotient + (remainder > j - current_line_start))
                current_line += words[current_line_start + current_line_count - 1]
            else:
                current_line = words[current_line_start]
                current_line += ' ' * (maxWidth - len(current_line))
            output_lines.append(current_line)
            # Reset for Next Line
            current_line_start = scanner
            current_line_count = 0
            current_line_len = 0
            current_blk_count = -1
    # Last Line
    if current_line_count > 0:   # still processing last line
        current_line = ' '.join(words[current_line_start:])
    else:  # last line processed, need to re-justify
        current_line = ' '.join(output_lines[-1].split())
    current_line += ' ' * (maxWidth - len(current_line))
    output_lines.append(current_line)
    return output_lines

print(fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification.",], maxWidth = 16))
print(fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
print(fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))

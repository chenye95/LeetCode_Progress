"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard
 for your reference

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and
 the number second.
"""


def square_is_white(coordinates: str) -> int:
    """
    :param coordinates: a lowercase letter follow by a number representing a square in chessboard
        'a' <= coordinates[0] <= 'h' and
        '1' <= coordinates[1] <= '8'
    :return: whether the square is white
    """
    return (ord(coordinates[0]) - ord('a') + int(coordinates[1]) - 1) % 2 == 1


test_cases = [("a1", False), ("h3", True), ("c7", False), ]
for test_coordinates, expected_output in test_cases:
    assert square_is_white(test_coordinates) is expected_output

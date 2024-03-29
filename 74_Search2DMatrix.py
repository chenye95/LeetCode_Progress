"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the
 following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
from typing import List

_not_found = -1


def binary_search_helper(target: int, array: List[int], force_equal: bool) -> int:
    """
    :param target: target number to find
    :param array: sorted array to search from
    :param force_equal: determines needs to find the exact target number
    :return: the position of target in array.
        If not found, returns -1 if not force_equal; else biggest number that is smaller than target
    """
    floor_id = _not_found
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if target > array[mid_pointer]:
            left_pointer = mid_pointer + 1
            floor_id = mid_pointer
        elif target < array[mid_pointer]:
            right_pointer = mid_pointer - 1
        else:
            return mid_pointer
    return _not_found if force_equal else floor_id


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if matrix and matrix[0] and matrix[0][0] <= target <= matrix[-1][-1]:
        first_column = [row[0] for row in matrix]
        row_num = binary_search_helper(target, first_column, False)
        return binary_search_helper(target, matrix[row_num], True) > _not_found
    return False


test_cases = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 100, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[-8, -6, -5, -4, -2, -1, -1, 0, 2, 4, 5, 7, 7, 7, 7, 9, 9, 9, 9, 11],
      [12, 14, 15, 16, 18, 20, 20, 20, 21, 21, 22, 23, 23, 25, 25, 25, 26, 27, 29, 30],
      [31, 31, 32, 32, 33, 35, 37, 39, 39, 39, 40, 41, 43, 44, 46, 48, 48, 48, 48, 50],
      [52, 54, 55, 57, 57, 58, 58, 60, 62, 64, 65, 65, 65, 67, 69, 71, 71, 73, 74, 74],
      [75, 76, 78, 78, 80, 82, 82, 82, 84, 85, 85, 87, 87, 89, 90, 90, 91, 93, 93, 94],
      [96, 98, 100, 102, 104, 105, 107, 109, 111, 113, 113, 115, 115, 117, 119, 119, 120, 122, 122, 124],
      [126, 127, 128, 130, 130, 130, 130, 132, 132, 133, 134, 136, 137, 138, 140, 141, 141, 143, 144, 146],
      [148, 150, 151, 152, 154, 156, 157, 158, 159, 161, 161, 162, 162, 164, 164, 165, 167, 168, 169, 169],
      [171, 173, 173, 175, 176, 178, 179, 181, 182, 183, 184, 184, 184, 185, 186, 186, 186, 186, 187, 189],
      [190, 192, 192, 193, 195, 196, 197, 197, 198, 198, 198, 198, 198, 199, 201, 203, 204, 206, 208, 208],
      [209, 210, 211, 212, 212, 212, 214, 214, 216, 217, 218, 218, 219, 221, 222, 224, 225, 227, 229, 229],
      [230, 230, 230, 231, 233, 233, 234, 235, 237, 237, 238, 238, 240, 240, 242, 242, 244, 246, 246, 247],
      [249, 251, 252, 252, 254, 254, 256, 256, 257, 258, 259, 260, 260, 261, 263, 265, 266, 267, 267, 269],
      [271, 273, 273, 274, 274, 274, 276, 276, 276, 278, 279, 280, 280, 280, 282, 284, 284, 286, 286, 287],
      [289, 290, 290, 291, 293, 293, 293, 293, 295, 296, 296, 297, 298, 299, 299, 301, 302, 304, 306, 308],
      [309, 310, 311, 311, 312, 312, 314, 315, 317, 319, 320, 322, 323, 324, 324, 324, 326, 328, 329, 331],
      [332, 334, 335, 337, 337, 339, 341, 343, 345, 347, 348, 348, 348, 348, 348, 350, 350, 350, 351, 352],
      [353, 355, 355, 356, 357, 358, 360, 361, 361, 361, 362, 364, 364, 364, 365, 366, 368, 370, 370, 372],
      [374, 376, 378, 380, 382, 382, 383, 384, 385, 385, 387, 388, 388, 390, 392, 394, 394, 396, 397, 399],
      [400, 402, 403, 403, 405, 405, 407, 409, 411, 411, 413, 414, 415, 417, 418, 419, 419, 419, 421, 422]], 271, True),
    ([[-8], [-5], [-4], [-2], [0], [3], [4], [5], [6], [8], [9], [11], [13], [16], [18], [20], [23], [25], [26], [27],
      [29], [31], [32], [34], [37], [38], [41], [44], [46], [49], [51], [53], [56], [57], [58], [60], [63], [65], [68],
      [70], [73], [76], [77], [79], [82], [84], [87], [90], [92], [94]], 57, True),
    ([[-8, -7, -5, -5, -3, -1, -1, 1, 3, 4, 6, 6, 7, 7, 9, 11, 12, 13, 14, 16, 18],
      [19, 21, 22, 24, 26, 28, 28, 29, 29, 29, 30, 32, 34, 36, 36, 37, 38, 40, 41, 43, 45],
      [48, 49, 50, 52, 52, 54, 55, 55, 57, 57, 58, 60, 62, 62, 64, 65, 67, 69, 69, 71, 72],
      [75, 77, 77, 79, 80, 81, 83, 85, 87, 87, 89, 89, 90, 92, 94, 95, 95, 97, 98, 100, 100],
      [102, 103, 105, 105, 105, 106, 108, 108, 109, 109, 109, 109, 111, 112, 113, 113, 114, 114, 116, 117, 117],
      [119, 119, 119, 119, 121, 121, 121, 122, 124, 125, 127, 128, 128, 128, 130, 131, 132, 132, 134, 136, 137],
      [138, 139, 141, 142, 144, 146, 146, 148, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 159, 160],
      [161, 162, 164, 164, 165, 165, 165, 166, 166, 167, 169, 170, 172, 172, 173, 174, 174, 175, 177, 178, 178],
      [180, 182, 184, 186, 188, 189, 191, 192, 194, 195, 197, 198, 199, 201, 201, 202, 204, 205, 206, 207, 207],
      [209, 210, 211, 213, 215, 217, 218, 220, 222, 224, 224, 226, 228, 229, 230, 230, 230, 232, 233, 235, 237],
      [238, 238, 239, 239, 241, 242, 243, 245, 246, 248, 248, 250, 251, 251, 253, 253, 255, 257, 257, 259, 259],
      [260, 261, 262, 263, 265, 267, 269, 269, 271, 272, 273, 273, 273, 274, 276, 278, 278, 280, 280, 280, 282],
      [283, 284, 284, 284, 286, 286, 288, 288, 290, 292, 292, 293, 295, 297, 297, 298, 299, 301, 302, 303, 303],
      [305, 307, 307, 308, 309, 310, 311, 311, 312, 312, 312, 312, 313, 313, 315, 316, 316, 316, 317, 317, 318],
      [321, 323, 324, 325, 325, 325, 326, 328, 330, 332, 332, 334, 336, 338, 339, 339, 340, 342, 344, 345, 347],
      [350, 351, 351, 351, 351, 352, 353, 355, 356, 356, 358, 359, 361, 362, 363, 363, 365, 367, 368, 368, 370],
      [371, 371, 373, 374, 376, 376, 377, 378, 378, 379, 381, 383, 384, 386, 388, 390, 391, 393, 394, 396, 398],
      [399, 400, 401, 403, 403, 405, 406, 407, 409, 410, 411, 413, 414, 415, 416, 418, 420, 421, 421, 422, 422],
      [425, 425, 425, 426, 427, 428, 429, 429, 430, 431, 431, 431, 431, 433, 434, 436, 437, 439, 440, 440, 441],
      [444, 445, 445, 446, 446, 448, 450, 451, 452, 452, 452, 454, 454, 454, 455, 455, 457, 458, 459, 460, 461],
      [464, 465, 466, 467, 468, 470, 470, 470, 472, 474, 474, 475, 475, 475, 477, 478, 480, 481, 483, 483, 485],
      [488, 489, 489, 489, 490, 492, 494, 494, 495, 496, 496, 496, 496, 497, 499, 501, 503, 503, 503, 503, 505],
      [507, 507, 509, 510, 511, 512, 512, 514, 516, 516, 518, 520, 521, 522, 522, 523, 523, 524, 524, 526, 528],
      [530, 532, 533, 533, 535, 535, 537, 539, 540, 541, 542, 542, 542, 543, 545, 547, 548, 550, 550, 552, 554],
      [557, 558, 558, 558, 558, 559, 560, 560, 561, 561, 563, 564, 565, 565, 566, 566, 568, 569, 571, 572, 573],
      [576, 578, 580, 580, 582, 582, 584, 584, 585, 587, 589, 591, 593, 595, 595, 597, 599, 600, 600, 602, 603],
      [606, 608, 608, 609, 609, 611, 613, 615, 617, 617, 617, 618, 620, 620, 621, 622, 622, 623, 625, 625, 625],
      [628, 628, 629, 629, 631, 631, 632, 633, 633, 634, 634, 634, 635, 637, 637, 638, 639, 639, 639, 639, 640],
      [643, 643, 644, 644, 646, 648, 650, 651, 653, 653, 654, 655, 657, 658, 659, 659, 660, 662, 663, 665, 665],
      [668, 668, 670, 670, 671, 673, 674, 674, 676, 678, 678, 680, 681, 681, 683, 683, 683, 684, 685, 687, 688],
      [691, 692, 692, 692, 694, 696, 696, 697, 698, 699, 699, 701, 702, 703, 705, 705, 707, 709, 709, 710, 712],
      [713, 713, 713, 713, 714, 716, 718, 720, 721, 722, 724, 724, 725, 727, 727, 729, 729, 731, 731, 733, 734],
      [736, 736, 738, 738, 739, 741, 741, 742, 743, 743, 745, 745, 745, 745, 746, 746, 746, 747, 748, 749, 749],
      [750, 750, 752, 753, 755, 756, 757, 758, 758, 760, 762, 763, 765, 765, 767, 769, 770, 771, 773, 774, 775]], 281,
     False),
]

for test_matrix, test_target, expected_value in test_cases:
    assert search_matrix(test_matrix, test_target) is expected_value

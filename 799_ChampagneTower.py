"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th
 row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid
 poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any
 excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has
 its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured,
 the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full
 - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half
 full, and the two outside glasses are a quarter full, as pictured below.
"""


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    """
    :param poured: 0 <= poured <= 1e9
    :param query_row: 0 <= query_glass <= query_row < 100
    :param query_glass: 0 <= query_glass <= query_row < 100
    :return: liquid left in query_glass_th glass in the query_row_th row
    """
    previous_row = [poured]
    for current_r in range(1, query_row + 1):
        current_row = [0.] * (current_r + 1)
        for c in range(current_r):
            if previous_row[c] > 1.:
                spill_over = (previous_row[c] - 1.) / 2
                current_row[c] += spill_over
                current_row[c + 1] += spill_over
        previous_row = current_row

    return min(1., previous_row[query_glass])


test_cases = [(1, 1, 1, 0.),
              (1, 0, 0, 1.),
              (2, 1, 0, .5),
              (2, 1, 1, .5),
              (100000009, 33, 17, 1.),
              (100, 85, 39, 0.), ]
for test_poured, test_row, test_glass, expected_value in test_cases:
    assert champagne_tower(test_poured, test_row, test_glass) == expected_value

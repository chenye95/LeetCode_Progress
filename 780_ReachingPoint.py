"""
A move consists of taking a point (x, y) and transforming it to either (x, x + y) or (x + y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to
 transform the point (sx, sy) to (tx, ty). Otherwise, return False.
"""


def reaching_points(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    :param sx: starting point (sx, sy), in range [1, 1000_000_000]
    :param sy: starting point (sx, sy), in range [1, 1000_000_000]
    :param tx: target ending point (tx, ty), in range [1, 1000_000_000]
    :param ty: target ending point (tx, ty), in range [1, 1000_000_000]
    :return: can move from starting point (sx, sy) to target point (tx, ty)
    """
    while sx < tx and sy < ty:
        # reduce the larger dimension by the other side
        if tx < ty:
            ty %= tx
        else:
            tx %= ty

    return sx == tx and sy <= ty and (ty - sy) % tx == 0 or \
           sy == ty and sx <= tx and (tx - sx) % ty == 0


test_cases = [(1, 1, 3, 5, True),
              (1, 1, 2, 2, False),
              (1, 1, 1, 1, True),
              (12, 17, 197, 70, False),
              (11, 33, 121, 198, True),
              (44, 43, 921197891, 702724365, True),
              (35, 13, 455955547, 420098884, False), ]
for test_sx, test_sy, test_tx, test_ty, expected_output in test_cases:
    assert reaching_points(test_sx, test_sy, test_tx, test_ty) is expected_output

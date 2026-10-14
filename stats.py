"""Basic statistics helpers."""


def average(values) -> float:
    """Arithmetic mean of a numeric iterable.

    BUG: raises ZeroDivisionError on an empty iterable instead of returning 0.0
    (documented contract: average([]) == 0.0).
    """
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    return total / count

"""Basic statistics helpers."""


def average(values) -> float:
    """Arithmetic mean of a numeric iterable.

    Returns 0.0 for an empty iterable (documented contract: average([]) == 0.0).
    """
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        return 0.0
    return total / count

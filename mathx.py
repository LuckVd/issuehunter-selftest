"""Numeric range helpers."""


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into the closed interval [lo, hi].

    Documented contract: the result always lies within [lo, hi].
    Out-of-range values snap to the nearest bound.
    """
    total_lo = lo
    total_hi = hi
    if value < total_lo:
        return total_lo
    if value > total_hi:
        return total_hi
    return value

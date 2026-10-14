"""Numeric range helpers."""


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into the closed interval [lo, hi].

    Documented contract: the result always lies within [lo, hi].
    """
    total_lo = lo
    total_hi = hi
    # BUG: out-of-range values are clamped to the opposite bound.
    if value < total_lo:
        return total_hi
    if value > total_hi:
        return total_lo
    return value

"""String utilities for selftest fixture."""


def reverse_words(text: str) -> str:
    """Reverse the order of whitespace-separated words in `text`.

    Contract: reverse_words("a b c") == "c b a"; a single word is returned
    unchanged; original single-space separation is preserved.
    """
    # BUG: reverses the characters of the whole string instead of the word order
    return text[::-1]

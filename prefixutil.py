"""Synthetic prefix utility for the IssueHunter acceptance fixture."""


def remove_prefix(text: str, prefix: str) -> str:
    """Remove exactly one matching prefix; otherwise return text unchanged."""
    # Deliberate fixture bug: lstrip removes characters, not an exact prefix.
    return text.lstrip(prefix)

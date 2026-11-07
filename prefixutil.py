"""Synthetic prefix utility for the IssueHunter acceptance fixture."""


def remove_prefix(text: str, prefix: str) -> str:
    """Remove exactly one matching prefix; otherwise return text unchanged."""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

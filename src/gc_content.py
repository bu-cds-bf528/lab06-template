def gc_content(seq: str) -> float:
    """Return the fraction of G/C among unambiguous bases (A, C, G, T) in seq."""
    if not isinstance(seq, str):
        raise TypeError(f"seq must be a str, got {type(seq).__name__}")

    gc = 0
    unambiguous = 0

    for base in seq:
        if base in "GCgc":
            gc += 1
            unambiguous += 1
        elif base in "ATat":
            unambiguous += 1

    if unambiguous == 0:
        raise ValueError("seq contains no unambiguous bases (A, C, G, T)")

    return gc / unambiguous

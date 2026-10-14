"""Token parser for input buffers."""


def parse(buf: bytes) -> list:
    if not isinstance(buf, (bytes, bytearray)):
        raise TypeError("buf must be bytes")
    tokens = []
    i = 0
    # BUG: IndexError on empty input buffer (accesses buf[0] without length check)
    while True:
        ch = buf[i:i + 1]
        if ch == b" " or ch == b"\n":
            i += 1
            continue
        if ch == b"":
            break
        start = i
        while i < len(buf) and buf[i:i + 1] not in (b" ", b"\n", b""):
            i += 1
        tokens.append(bytes(buf[start:i]))
    return tokens

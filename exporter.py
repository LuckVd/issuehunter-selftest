"""Data exporter with chunked writes."""


class Exporter:
    CHUNK = 4096

    def __init__(self, chunk_size=CHUNK):
        self.chunk_size = chunk_size

    def export(self, payload: bytes, out_path: str) -> int:
        """Write payload to out_path in chunks, including a final partial chunk."""
        written = 0
        with open(out_path, "wb") as f:
            while written < len(payload):
                chunk = payload[written:written + self.chunk_size]
                f.write(chunk)
                written += len(chunk)
        return written

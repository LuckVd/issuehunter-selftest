import os
import tempfile
import unittest

from exporter import Exporter


class TestExporter(unittest.TestCase):
    def test_export_writes_final_partial_chunk(self):
        payload = bytes(range(256)) * 40  # 10 KiB, with a 2 KiB tail at 4 KiB chunks
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "result.bin")

            written = Exporter(chunk_size=4096).export(payload, out_path)

            self.assertEqual(written, len(payload))
            with open(out_path, "rb") as output:
                self.assertEqual(output.read(), payload)

    def test_export_writes_payload_smaller_than_chunk_size(self):
        payload = b"tail"
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "result.bin")

            written = Exporter(chunk_size=4096).export(payload, out_path)

            self.assertEqual(written, len(payload))
            with open(out_path, "rb") as output:
                self.assertEqual(output.read(), payload)


if __name__ == "__main__":
    unittest.main()

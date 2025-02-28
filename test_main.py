import subprocess
import sys
import unittest


class TestSQLGlotCLI(unittest.TestCase):
    def test_transpile(self):
        cases = [
            {
                "name": "flagshipGnnEmbedding300",
                "source": "SELECT embedding['tensor']['staticDense']['values']['floats'] as flagshipGnnEmbedding300 from tracking.FeedIndexingGNNActivityEmbedding",
                "target": "SELECT embedding['tensor']['staticDense']['values']['floats'] AS flagshipGnnEmbedding300 FROM tracking.FeedIndexingGNNActivityEmbedding",
            }
        ]

        for case in cases:
            with self.subTest(msg=case["name"]):
                process = subprocess.Popen(
                    [sys.executable, "main.py", case["source"]],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = process.communicate()
                self.assertEqual(stderr.decode().strip(), "")
                self.assertEqual(stdout.decode().strip(), case["target"])

if __name__ == "__main__":
    unittest.main()


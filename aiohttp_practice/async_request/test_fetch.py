import unittest
import fetch


class TestMain(unittest.TestCase):
    def test_save_results_first_time(self):
        self.assertEqual(fetch.save_results(), None)

    def test_save_results(self):
        self.assertEqual(fetch.save_results(), "Aarika")


if __name__ == "__main__":
    unittest.main()

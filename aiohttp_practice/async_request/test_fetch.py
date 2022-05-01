import unittest
import fetch


class TestMain(unittest.TestCase):
    def test_save_results(self):
        with open("data.json", "w") as f:
            pass
        self.assertEqual(len(fetch.save_results()), 2)
        self.assertEqual(len(fetch.save_results()), 4)


if __name__ == "__main__":
    unittest.main()

import unittest
import main

class Test(unittest.TestCase):
    def setUp(self):
        self.testcases = [
            {
                "actual": lambda: main.Solution().numIslands([
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"],
                ]),
                "expected": 1,
            },
            {
                "actual": lambda: main.Solution().numIslands([
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"],
                ]),
                "expected": 3,
            },
        ]

    def test(self):
        for testcase in self.testcases:
            actual = testcase["actual"]()
            expected = testcase["expected"]
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

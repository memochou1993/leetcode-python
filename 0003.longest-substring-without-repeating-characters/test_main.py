import unittest
import main

class Test(unittest.TestCase):
    def setUp(self):
        self.testcases = [
            {
                "actual": lambda: main.Solution().lengthOfLongestSubstring('abcabcbb'),
                "expected": 3,
            },
            {
                "actual": lambda: main.Solution().lengthOfLongestSubstring('bbbbb'),
                "expected": 1,
            },
            {
                "actual": lambda: main.Solution().lengthOfLongestSubstring('pwwkew'),
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

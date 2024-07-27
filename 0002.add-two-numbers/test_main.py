import unittest
import main
from utils import list_to_list_node, list_node_to_list

class Test(unittest.TestCase):
    def setUp(self):
        self.testcases = [
            {
                "actual": lambda: main.Solution().addTwoNumbers(list_to_list_node([2,4,3]), list_to_list_node([5,6,4])),
                "expected": list_to_list_node([7,0,8]),
            },
            {
                "actual": lambda: main.Solution().addTwoNumbers(list_to_list_node([0]), list_to_list_node([0])),
                "expected": list_to_list_node([0]),
            },
            {
                "actual": lambda: main.Solution().addTwoNumbers(list_to_list_node([9,9,9,9,9,9,9]), list_to_list_node([9,9,9,9])),
                "expected": list_to_list_node([8,9,9,9,0,0,0,1]),
            },
        ]

    def test(self):
        for testcase in self.testcases:
            actual = list_node_to_list(testcase["actual"]())
            expected = list_node_to_list(testcase["expected"])
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

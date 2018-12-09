import unittest
import solution_old


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution_old.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        test_str = 121
        result = self.solution.isPalindrome(test_str)
        print(result)
        self.assertTrue(result)

    def test_result2(self):
        test_str = -121
        result = self.solution.isPalindrome(test_str)
        print(result)
        self.assertFalse(result)

    def test_result3(self):
        test_str = 100
        result = self.solution.isPalindrome(test_str)
        print(result)
        self.assertFalse(result)




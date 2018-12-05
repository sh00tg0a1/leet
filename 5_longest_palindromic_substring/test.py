import unittest
import solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        test_str = "babad"
        result = self.solution.longestPalindrome(test_str)
        self.assertTrue(result == "bab" or result == "aba")

    def test_result2(self):
        test_str = "cbbd"
        result = self.solution.longestPalindrome(test_str)
        self.assertEqual(result, "bb")
    
    def test_result3(self):
        test_str = "abcdefedcba"
        result = self.solution.longestPalindrome(test_str)
        self.assertEqual(result, "abcdefedcba")

    def test_result4(self):
        test_str = "aaaa"
        result = self.solution.longestPalindrome(test_str)
        self.assertEqual(result, "aaaa")

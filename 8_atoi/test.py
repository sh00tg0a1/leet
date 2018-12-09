import unittest
import solution_old


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution_old.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        test_str = "42"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(42, result)

    def test_result2(self):
        test_str = "   -42"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(-42, result)

    def test_result3(self):
        test_str = "4193 with words"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(4193, result)

    def test_result4(self):
        test_str = "words and 987"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(0, result)

    def test_result5(self):
        test_str = "-91283472332"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(-2147483648, result)

    def test_result6(self):
        test_str = "+-2"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(0, result)

    def test_result7(self):
        test_str = "   +0 123"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(0, result)

    def test_result8(self):
        test_str = "-    234"
        result = self.solution.myAtoi(test_str)
        print(result)
        self.assertEqual(0, result)



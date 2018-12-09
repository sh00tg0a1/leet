import unittest
import solution_old


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution_old.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        test_str = 123
        result = self.solution.reverse(test_str)
        print(result)
        self.assertEqual(321, result)

    def test_result2(self):
        test_str = -123
        result = self.solution.reverse(test_str)
        print(result)
        self.assertEqual(-321, result)

    def test_result3(self):
        test_str = -2147483412
        result = self.solution.reverse(test_str)
        print(result)
        self.assertEqual(0, result)


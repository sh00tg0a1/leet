import unittest
import solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        result = self.solution.isMatch('aa', 'a')
        self.assertTrue(not result)

    def test_result2(self):
        result = self.solution.isMatch('aa', 'a*')
        self.assertTrue(result)

    def test_result3(self):
        result = self.solution.isMatch('ab', '.*')
        self.assertTrue(result)

    def test_result4(self):
        result = self.solution.isMatch('aab', 'c*a*b')
        self.assertTrue(result)

    def test_result5(self):
        result = self.solution.isMatch('mississippi', 'mis*is*p*.')
        self.assertTrue(not result)

    def test_result6(self):
        result = self.solution.isMatch('aaa', 'a*a')
        self.assertTrue(result)

    def test_result7(self):
        result = self.solution.isMatch('ab', '.*c')
        self.assertTrue(not result)

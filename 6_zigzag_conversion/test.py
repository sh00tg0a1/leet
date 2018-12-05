import unittest
import solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = solution.Solution()

    def tearDown(self):
        pass

    def test_result1(self):
        '''
        P A H N
        APLSIIG
        Y I R
        '''
        test_str = "PAYPALISHIRING"
        result = self.solution.convert(test_str, 3)
        print(result)
        self.assertEqual(result, 'PAHNAPLSIIGYIR')

    def test_result2(self):
        test_str = "PAYPALISHIRING"
        result = self.solution.convert(test_str, 4)
        print(result)
        self.assertEqual(result, "PINALSIGYAHRPI")

    def test_result3(self):
        test_str = "A"
        result = self.solution.convert(test_str, 3)
        print(result)
        self.assertEqual(result, "A")


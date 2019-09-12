import time
from s import Solution


class test(object):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_solution(self):
        assert(self.s.intToRoman(3) == 'III')

    def test_solution2(self):
        assert(self.s.intToRoman(4) == 'IV')

    def test_solution3(self):
        assert(self.s.intToRoman(9) == 'IX')

    def test_solution4(self):
        assert(self.s.intToRoman(58) == 'LVIII')

    def test_solution5(self):
        assert(self.s.intToRoman(1994) == 'MCMXCIV')

from s import Solution


class test(object):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_1(self):
        assert(self.s.numberToWords(1) == 'One')

    def test_123(self):
        assert(self.s.numberToWords(123) == 'One Hundred Twenty Three')

    def test_1234567(self):
        assert(self.s.numberToWords(1234567) == 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')

    def test_120(self):
        assert(self.s.numberToWords(120) == 'One Hundred Twenty')

    def test_101(self):
        assert(self.s.numberToWords(101) == 'One Hundred One')

    def test_big(self):
        assert(self.s.numberToWords(2**31 - 1) != 'One Hundred Twenty')
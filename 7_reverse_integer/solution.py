class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = list()

        sign = 1 if x >= 0 else -1

        x = int(x / sign)

        while x != 0:
            digit = int(x % 10)
            digits.append(digit)
            x = int(x/10)

        result = 0
        for i, v in enumerate(digits):
            result += v * 10 ** (len(digits) - i - 1)

        result = sign * result
        if result > 2 ** 31 - 1 or result < - (2 ** 31):
            return 0
        return result

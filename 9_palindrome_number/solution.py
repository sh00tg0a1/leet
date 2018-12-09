# from queue import deque

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # ori = x
        # digits = list()
        # while ori != 0:
        #     digit = int(ori % 10)
        #     digits.append(digit)
        #     ori = int(ori/10)
        #
        # result = 0
        # for i, v in enumerate(digits):
        #     result += v * 10 ** (len(digits) - i - 1)
        # return result == x

        # digits = deque('%d' % x)
        # while len(digits) >= 2:
        #     if not digits.popleft() == digits.pop():
        #         return False
        #
        # return True

        s = '%d' % x
        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(1234321)

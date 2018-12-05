#
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
#
import yappi

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        candidate = (0, 0)

        length = len(s)
        for i in range(1, 2 * length):
            left = int((i - 1) / 2) if i % 2 == 1 else int(i / 2 - 1)
            right = int((i + 1) / 2) if i % 2 == 1 else int(i / 2 + 1)

            while left >= 0 and right < length:
                if s[left] == s[right]:
                    if right - left > candidate[1] - candidate[0]:
                        candidate = (left, right)

                    left, right = left - 1, right + 1
                else:
                    break

            if (candidate[1] - candidate[0]) / 2 > length - left:
                break

        return s[candidate[0]:candidate[1] + 1]


if __name__ == "__main__":
    import cProfile

    test_str = "asdfadfasdfasdfghjklkjhgfdsaasdasfasdf"
    s = Solution()

    for i in range(1000):
        result = s.longestPalindrome(test_str)

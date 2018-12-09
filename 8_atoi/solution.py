class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        val_str = ""
        sign = 0
        result = 0

        for s in str:
            if s in '\t ':
                if val_str or sign:
                    break

                continue

            if not val_str:
                if s == "+":
                    if sign:
                        return result
                    sign = 1
                    continue
                if s == "-":
                    if sign:
                        return result
                    sign = -1
                    continue

                if ord(s) < ord('0') or ord(s) > ord('9'):
                    return result
                else:
                    val_str += s
                    if not sign:
                        sign = 1
            else:
                if ord('0') <= ord(s) <= ord('9'):
                    val_str += s
                else:
                    break

        for i, v in enumerate(val_str):
            result += (ord(v) - ord('0')) * 10 ** (len(val_str) - i -1)

        result *= sign

        sup, inf = 2 ** 31 - 1, -(2 ** 31)
        if result < inf:
            return inf
        if result > sup:
            return sup

        return result

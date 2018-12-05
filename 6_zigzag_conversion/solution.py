class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result = list()
        for i in range(numRows):
            result.append('')

        row_index = 0
        step = -1

        for a in s:
            if row_index % (numRows - 1) == 0:
                step *= -1

            result[row_index] += a
            row_index += step

        return ''.join(result)

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        if num > 3999 or num < 1:
            return 'error'

        k = int(num / 1000)
        if k != 0:
            res += k * 'M'
            num = num % 1000

        h = int(num / 100)

        if h != 0:
            num = num % 100
            if h == 4:
                res += 'CD'
            elif h < 4:
                res += 'C' * h
            elif h == 5:
                res += 'D'
            elif h == 9:
                res += 'CM'
            else:
                res += 'D' + (h - 5) * 'C'

        d = int(num / 10)
        if d != 0:
            num = num % 10
            if d == 4:
                res += 'XL'
            elif d < 4:
                res += 'X' * d
            elif d == 5:
                res += 'L'
            elif d == 9:
                res += 'XC'
            else:
                res += 'L' + (d - 5) * 'X'

        if num != 0:
            if num == 4:
                res += 'IV'
            elif num < 4:
                res += 'I' * num
            elif num == 5:
                res += 'V'
            elif num == 9:
                res += 'IX'
            else:
                res += 'V' + (num - 5) * 'I'

        return res

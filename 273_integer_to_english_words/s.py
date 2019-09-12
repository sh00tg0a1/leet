class Solution:
    word_map = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        15: 'Fifteen',
        18: 'Eighteen'
    }

    word_map2 = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        8: 'Eighty'
    }

    def getWord(self, n):
        res = ''
        h = int(n / 100)

        if h != 0:
            n %= 100
            res += self.word_map[h] + ' Hundred '

        if n != 0:
            # res += 'and '
            if n in self.word_map:
                res += self.word_map[n]
            else:
                if n < 20:
                    res += self.word_map[n % 10] + 'teen'
                else:
                    a = int(n / 10)
                    n %= 10

                    if a in self.word_map2:
                        res += self.word_map2[a] + ' '
                    else:
                        res += self.word_map[a] + 'ty '

                    if n != 0:
                        res += self.word_map[n]
        return res.strip(' ')

    def numberToWords(self, num: int) -> str:
        res = ''
        if num > 2 ** 31 - 1:
            return 'error'

        if num == 0:
            return 'Zero'

        b = int(num / 1000000000)
        if b != 0:
            num %= 1000000000
            res += self.getWord(b) + ' Billion '

        m = int(num / 1000000)

        if m != 0:
            num %= 1000000
            res += self.getWord(m) + ' Million '

        k = int(num / 1000)

        if k != 0:
            num %= 1000
            res += self.getWord(k) + ' Thousand '

        res += self.getWord(num)
        res = res.strip(' ')

        # print(res)
        return res


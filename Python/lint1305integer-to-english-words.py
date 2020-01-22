class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        look = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ];
        look2 = {20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety',
                 1:'', 100:'Hundred', 1000:'Thousand', 10**6:'Million', 10**9:'Billion'}
        def convert(d):
            ret = ''
            hs = d / 100
            if hs:
                ret += '{} {} '.format(look[hs], look2[100])
            d %= 100
            if 0 < d < 20:
                return ret + '{}'.format(look[d])
            else:
                ones = d % 10
                tens = d - ones
                ret += '{}'.format(look2[tens])
                if ones > 0:
                    ret += ' {}'.format(look[ones])
            return ret.strip()

        if num == 0: return 'Zero'
        ans = ''
        for i in [9,6,3,0]:
            factor = 10**i
            bs = num / factor
            if bs:
                ans += ' {} {}'.format(convert(bs), look2[factor])
            num %= factor

        return ans.strip()

print Solution().numberToWords(680901192)
print Solution().numberToWords(123)
print Solution().numberToWords(123456789)
print Solution().numberToWords(1002038903)
''' 273. Integer to English Words
Hard    2412    5543    Add to List     Share
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:    0 <= num <= 2^31 - 1
Accepted:       328,274
Submissions:    1,098,769
'''


class Solution:
    def numberToWords(self, num: int) -> str:
        dic = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five',
               6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven',
               12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen',
               16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen',
               20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty',
               70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred',
               1000:'Thousand', 1000000:'Million', 1000000000:'Billion',
               1000000000000:'Trillion'}
        if num == 0: return dic[0]
        res = []

        def lessThan1000(num: int) -> str:
            if num == 0: return ''
            res = []
            if num > 999: return 'Error'
            p1 = num % 10
            p10 = num % 100
            if p10 != 0:
                if p10 == 0: res.append()
                elif p10 < 21:
                    res.append(dic[p10])
                else:
                    p10 = num % 100 // 10 * 10            
                    res.append(dic[p10])

                    if p1 > 0:
                        res.append(dic[p1])

            p100 = num % 1000 // 100
            if p100 > 0:
                temp = [dic[p100], dic[100]]
                if len(res) > 0:
                    res = temp + res
                else:
                    res = temp
            return ' '.join(res)
        
        if num < 1000: return lessThan1000(num)
        elif num < 1000000:
            res = lessThan1000(num // 1000)+' '+dic[1000]
            if lessThan1000(num % 1000):
                res += ' '+lessThan1000(num % 1000)
            
        elif num < 1000000000:
            res = lessThan1000(num // 1000000)+' '+dic[1000000]
            if lessThan1000(num % 1000000 // 1000):
                res += ' '+lessThan1000(num % 1000000 // 1000)+' '+ dic[1000]
            if lessThan1000(num % 1000):
                res += ' '+lessThan1000(num % 1000)
                
        elif num < 1000000000000:
            res = lessThan1000(num // 1000000000)+' '+dic[1000000000]
            if lessThan1000(num % 1000000000 // 1000000):
                res += ' '+lessThan1000(num % 1000000000 // 1000000)+' '+dic[1000000]
            if lessThan1000(num % 1000000 // 1000):
                res += ' '+lessThan1000(num % 1000000 // 1000)+' '+ dic[1000]
            if lessThan1000(num % 1000):
                res += ' '+lessThan1000(num % 1000)

        return res


def main():
    sol = Solution()
    print(sol.numberToWords(0))             # "Zero"
    print(sol.numberToWords(12))            # "Twelve"
    print(sol.numberToWords(123))           # "One Hundred Twenty Three"
    print(sol.numberToWords(12345))         # "Twelve Thousand Three Hundred Forty Five"
    print(sol.numberToWords(1234567))       # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(sol.numberToWords(1234567891))    # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    print(sol.numberToWords(1000))          # "One Thousand"
    print(sol.numberToWords(10000000))      # "Ten Million"

main()

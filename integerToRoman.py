class Solution:
    def intToRomanDirectEncode(self, num: int) -> str:
        M = ["","M","MM","MMM"]
        C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return M[num//1000] + C[(num//100)%10] + X[(num//10)%10] + I[num%10]

    def intToRoman(self, num: int) -> str:
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanNumber = ""
        for i, j in enumerate(nums):
            while num >= j:
                romanNumber += strs[i]
                num -= j
            if num == 0:
                return romanNumber
solution = Solution()
print(solution.intToRoman(794))


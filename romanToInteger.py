class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        romanConversionDict = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }
        romanNumeralList = romanConversionDict.keys()
        romanNumeralLength = len(s)
        i = 0
        while(i < romanNumeralLength):
            if(
                i < romanNumeralLength and
                s[i] in ['I', 'X', 'C'] and
                s[i:i+2] in romanNumeralList
            ):
              sum += romanConversionDict[s[i:i+2]]
              i+=2
            else:
              sum += romanConversionDict[s[i]]
              i+=1
        return sum

    def romanToIntV2(self, s: str) -> int:
        romanConversionDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        for i in range(0, len(s) - 1):
            if(romanConversionDict[s[i]] < romanConversionDict[s[i+1]]):
                sum -= romanConversionDict[s[i]]
            else:
                sum += romanConversionDict[s[i]]
        return sum + romanConversionDict[s[-1]]

solution = Solution()
print(solution.romanToIntV2('III'))
print(solution.romanToIntV2('IV'))
print(solution.romanToIntV2('IX'))
print(solution.romanToIntV2('LVIII'))
print(solution.romanToIntV2('MMCMXCIV'))

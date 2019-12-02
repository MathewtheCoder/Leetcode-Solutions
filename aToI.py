class Solution:
    def extractInteger(self, str: str) -> int:
        # in case only '+' or '-' or '-a'
        if(len(str) == 1 or not str[1].isnumeric()):
            return 0
        if(str[0] == '+' or str[0] == '-'):
            sign = str[0]
        else:
            sign = ''
        temp = str[1::]
        for index, letter in enumerate(temp):
            if not letter.isnumeric():
                return sign + temp[:index:]
        return sign + temp




    def myAtoi(self, str: str) -> int:
        trimmedString = str.strip()
        if(trimmedString[0] == '+' or trimmedString[0] == '-'):
            sign = trimmedString[0]
            temp = trimmedString[1::]
        elif not trimmedString[0].isnumeric():
            return 0
        else:
            sign = ''
            temp = trimmedString
        print(temp)
        for index, value in enumerate(temp):
            # print(index, value)
            if not value.isnumeric():
                temp = int(sign + temp[:index])
                break
        if(sign):
            return int(sign + temp)

        return temp if temp.isnumeric() else 0




s = Solution()
# print(s.myAtoi("     -41")) # True
print(s.myAtoi("   +   a123  ")) # False
# print(s.myAtoi("     +41asas")) # False
# print(s.myAtoi("     -412")) # True
# print(s.myAtoi("     -a41    ")) # False
# print(s.myAtoi("     asas")) # False

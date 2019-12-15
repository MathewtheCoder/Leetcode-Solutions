# Valid parathesis
class Solution:
    def isValidAscii(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol in ['(', '[', '{']:
                stack.append(symbol)
            else:
                if not len(stack):
                    return False
                temp = stack.pop()
                if(
                    ord(temp) != ord(symbol) - 2 and
                    ord(temp) != ord(symbol) - 1
                ):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()

print(s.isValid("}"))
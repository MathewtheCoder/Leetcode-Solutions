# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
from typing import List
class Solution:
    def longestCommonPrefixNaive(self, strs: List[str]) -> str:
        commonPrefix = ""
        #in case of empty list return empty string
        if(len(strs) == 0):
            return commonPrefix
        commonPrefix = strs.pop(0)
        # in case of single string return first string itself
        if(len(strs) == 0):
            return commonPrefix
        # Compare first String with rest of string and find common prefix
        for word in strs:
            wordLength = len(word)
            commonPrefixLength = len(commonPrefix)
            # if len of word is greater than common prefix slice it and compare
            if(wordLength > commonPrefixLength):
                if(word[0 : commonPrefixLength : 1] == commonPrefix):
                    commonPrefix = word[0 : commonPrefixLength : 1]
                    continue
                i = 1
                while(commonPrefixLength - i > 0):
                    commonPrefix = commonPrefix[0 : commonPrefixLength - i : 1]
                    newSlice = word[0 : commonPrefixLength - i : 1]
                    if(newSlice == commonPrefix):
                        break
                    i+=1
                else:
                    return ""
            else:
                if(commonPrefix[0 : wordLength : 1] == word):
                    commonPrefix = commonPrefix[0 : wordLength : 1]
                    continue
                i = 1
                while(wordLength - i > 0):
                    commonPrefix = commonPrefix[0 : wordLength - i : 1]
                    newSlice = word[0 : wordLength - i : 1]
                    if(newSlice == commonPrefix):
                        break
                    i+=1
                else:
                    return ""
        return commonPrefix
    # Best solution found in discussion
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight", "fwewewe"]))
print(s.longestCommonPrefixNaive(["dog","racecar","car"]))


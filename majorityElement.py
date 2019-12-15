from typing import List
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element
# always exist in the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        length = len(nums)//2
        for ele in nums:
            if ele not in hashMap.keys():
                hashMap[ele] = 1
            else:
                hashMap[ele] += 1
                if hashMap[ele] > length:
                    return ele
        for i in hashMap.keys():
            if hashMap[i] > length:
                return i


s = Solution()
print(s.majorityElement([2,2,1,1,2,2]))
from typing import List
class Solution:
    def majorityElementV1(self, nums: List[int]) -> List[int]:
        hashMap = {}
        length = len(nums)//3
        majorCandidates = []
        for ele in nums:
            if ele not in hashMap.keys():
                hashMap[ele] = 1
                if hashMap[ele] > length:
                    majorCandidates.append(ele)
            else:
                hashMap[ele] += 1
                if ele not in majorCandidates and hashMap[ele] > length:
                    majorCandidates.append(ele)
        return majorCandidates
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

s = Solution()
print(s.majorityElement([1,1,1,1,3,3,3,3,2,2,2,2]))

class Solution:
    def twoSumNaive(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if(i == j):
                    continue
                if(nums[i] + nums[j] == target):
                    return [i, j]
    def twoSumFinal(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]
            lookup[target - nums[i]] = i



test = Solution()
print(test.twoSumV2([0,4,3,0], 0))
print(test.twoSumV2([3,2,4], 6))
print(test.twoSumV2([3,3], 6))
print(test.twoSumV2([1,3,7,2,9], 9))
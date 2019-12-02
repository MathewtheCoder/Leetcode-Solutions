# Peak Index in a Mountain Array
# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain,
# return any i such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
from typing import List
import math

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lowerEnd = 0
        upperEnd = len(A)
        while lowerEnd < upperEnd:
            mid = math.floor((lowerEnd + upperEnd) / 2)
            if(A[mid] > A[mid - 1] and A[mid] > A[mid+1]):
                return mid
            elif(A[mid] < A[mid - 1]):
                upperEnd = mid
            elif(A[mid] <= A[mid + 1]):
                lowerEnd = mid + 1



solution = Solution()
print(solution.peakIndexInMountainArray([0,2,1,0]))
print(solution.peakIndexInMountainArray([1,3,4,6,7,8,9,10,5,4,2,1]))
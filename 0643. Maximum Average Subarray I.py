# O(n) complexity
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curserSum = 0

        for i in range(0, k):
            curserSum += nums[i]

        maxAverage = curserSum/k

        for i in range(k, n):
            curserSum += nums[i] - nums[i-k]
            currentAverage = curserSum/k
            maxAverage = max(maxAverage, currentAverage)

        return round(maxAverage, 5)

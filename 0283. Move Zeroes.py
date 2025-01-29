#Inefficient O(n²) solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]



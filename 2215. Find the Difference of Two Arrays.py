# Complexity O(n)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniqueElements1 = []
        uniqueElements2 = []
        
        set1 = set(nums1)
        set2 = set(nums2)

        commonElements = set1 & set2
        uniqueElements1 = set1 - commonElements
        uniqueElements2 = set2 - commonElements

        return [list(uniqueElements1), list(uniqueElements2)]

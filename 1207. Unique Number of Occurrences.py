# 0 ms runtime
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = set()
        arrSet = set(arr)
        for num in arrSet:
            if arr.count(num) in count:
                return False
            count.add(arr.count(num))
        return True

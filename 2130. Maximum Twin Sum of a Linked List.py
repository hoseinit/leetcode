class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None or head.next is None:
            return 0
        
        values = []

        while head:
            values.append(head.val)
            head = head.next
        max = 0
        n = len(values)
        for i in range(n//2):
            value = values[i] + values[n - i - 1]
            if  value > max:
                max = value
        return max

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l1=[]
        count = 0
        while head :
            l1.append (head.val)
            count += 1
            head = head.next
        
        l,r = 0, count -1
        max= -999999
        while l < r:
            add = l1[l]+l1[r]
            if  add > max: max = add
            l += 1
            r -= 1
        return max

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []
        curr = head
        count = 0
        while curr:
            #if count <=
            l1.append(curr.val)
            count += 1
            print(curr.val)
            curr = curr.next
        for i in range(count//2):
            if l1[i] != l1[count-i-1]:return False
        return True

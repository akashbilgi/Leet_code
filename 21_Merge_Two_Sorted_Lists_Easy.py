# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        newlist = ListNode()
        ll = newlist
        while list1 and list2:
            if list1.val <= list2.val:
                ll.next = ListNode(list1.val)
                list1 = list1.next            
            else:
                ll.next = ListNode(list2.val)
                list2 = list2.next
            ll = ll.next
        while list1: 
            ll.next = ListNode(list1.val)
            list1 =list1.next
            ll =ll.next
        while list2:
            ll.next = ListNode(list2.val)
            list2 =list2.next
            ll =ll.next
        return newlist.next

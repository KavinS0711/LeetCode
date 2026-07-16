# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        a = list1
        while a != None:
            x.append(a.val)
            a = a.next

        y = []
        a = list2
        while a != None:
            y.append(a.val)
            a = a.next

        z = x.copy()
        z.extend(y)
        z.sort()

        if not z:
            return None

        list3 = ListNode(z[0])
        b = list3
        for i in range(1,len(z)):
            b.next = ListNode(z[i])
            b = b.next

        return list3
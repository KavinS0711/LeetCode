# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = head
        while b != None:
            a.append(b.val)
            b = b.next
        

        out = []
        for i in a:
            if i not in out:
                out.append(i)
        out.sort()

        if not out: return None

        ret = ListNode(out[0])
        z = ret
        for i in range(1,len(out)):
            z.next = ListNode(out[i])
            z = z.next
        
        return ret

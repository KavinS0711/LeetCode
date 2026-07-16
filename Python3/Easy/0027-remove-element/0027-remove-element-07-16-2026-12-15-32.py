class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        b = nums.copy()
        for i in b:
            if i != val:
                nums.insert(0,i)
        a = b.count(val)
        a = len(b)-a
        return(a)
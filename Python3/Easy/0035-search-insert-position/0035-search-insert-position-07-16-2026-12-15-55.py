class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        for i in nums:
            if target <= i:
                return a
            else: a+=1
        return a

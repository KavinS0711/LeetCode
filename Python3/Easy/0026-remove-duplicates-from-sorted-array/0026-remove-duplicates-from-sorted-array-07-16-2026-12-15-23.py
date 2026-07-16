class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out = []

        for i in nums:
            if i not in out:
                out.append(i)

        for i in range(len(out)):
            nums[i] = out[i]

        return len(out)
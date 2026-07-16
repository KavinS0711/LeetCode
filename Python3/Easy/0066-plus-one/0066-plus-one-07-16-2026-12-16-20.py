class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        l=[]
        for i in digits:
            a += str(i)
        out = str(int(a)+1)
        for i in out:
            l.append(int(i))
        return l
        
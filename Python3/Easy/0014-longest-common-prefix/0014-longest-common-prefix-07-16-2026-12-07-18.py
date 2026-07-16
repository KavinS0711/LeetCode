class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        
        if not strs:
            return out
        
        for i in range(len(strs[0])):
            x = strs[0][:i+1]
            for y in strs:
                if y.startswith(x):
                    pass
                else:
                    return out
            out = x
        return out

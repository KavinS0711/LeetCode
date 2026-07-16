# ([])()

class Solution:
    def isValid(self, s: str) -> bool:
        ink = list(s)
        out = []
        for i in ink:
            if i in "([{":
                out.append(i)
            elif i == ")":
                if out and out[-1] == "(":
                    out.pop()
                else:return False
            elif i == "]":
                if out and out[-1] == "[":
                    out.pop()
                else:return False
            elif i == "}":
                if out and out[-1] == "{":
                    out.pop()
                else: return False

        if out == []:
            return True
        else: return False

        
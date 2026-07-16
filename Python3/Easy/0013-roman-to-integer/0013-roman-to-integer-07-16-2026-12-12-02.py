class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            try:   
                if s[i] == "I":
                    try: 
                        if s[i+1] in "VX":
                            out -= 1
                        else: out += 1
                    except: 
                        out +=1
                        return out

                elif s[i] == "V":
                    out += 5

                elif s[i] == "X":
                    try: 
                        if s[i+1] in "LC":
                            out -= 10
                        else: out += 10
                    except:
                        out += 10
                        return out

                elif s[i] == "L": out += 50

                elif s[i] == "C": 
                    try:
                        if s[i+1] in "DM":
                            out -= 100
                        else: out += 100
                    except:
                        out += 100
                        return out

                elif s[i] == "D": out += 500

                else: out += 1000
            except:
                return out
        return out

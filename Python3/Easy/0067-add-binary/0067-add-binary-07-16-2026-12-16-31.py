class Solution:
    def addBinary(self, a: str, b: str) -> str:
        z = int(a) + int(b) #12
        z = list(str(z))
        z = z[::-1]  #21
        for i in range(len((z))-1):
            if int(z[i]) > 1:
                z[i+1] = int(z[i+1]) + 1
                z[i] = int(z[i])%2
        if int(z[-1]) > 1:
            z[-1] = int(z[-1])%2
            z.append(1)
        out = ""
        for i in z:
            out += str(i)
        return out[::-1]

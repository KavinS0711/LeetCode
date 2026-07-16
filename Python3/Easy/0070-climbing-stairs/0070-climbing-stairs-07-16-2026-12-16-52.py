#to reach nth step i can either go frm n-1 or n-2

'''4
2+2: 1
2+1+1: 3
1+1+1+1: 1

0: 1
1: 1
2: 2
3: 1+2 = 3
4: 2+3 = 5
5: 3+5 = 8'''





class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        c = 1
        for i in range(1, n):
            c = a+b
            a=b
            b=c
        return c




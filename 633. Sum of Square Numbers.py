import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            a2 = l*1
            b2 = r*r
            if (a2 +b2==c):
                return True
            elif(a2 +b2 < c):
                    l+=1
            elif( a2 +b2 >c):
                r-=1
            else:
                return False



        

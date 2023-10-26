class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:  
                                                        # Ex: word1 = brsw        word2 = ehrap

        w1 =list(word1)
        w2 =list(word2) 
        ans = ''      # <--    w1 = [b,r,s,w]      w2 = [e,h,r,a,p]

        while w1 and w2:                                #  w1           w2           ans
            ans+= w1.pop(0) if w1 > w2 else w2.pop(0)   #  –––––––––    –––––––––    –––––
                                                        #  [b,r,s,w]    [h,r,a,p]    e
                                                        #  [b,r,s,w]    [r,a,p]      eh
                                                        #  [b,r,s,w]    [a,p]        ehr
                                                        #  [r,s,w]      [a,p]        ehrb
                                                        #  [s,w]        [a,p]        ehrbr
                                                        #  [w]          [a,p]        ehrbrs
                                                        #  []           [a,p]        ehrbrsw

        return  ans + ''.join(w1) + ''.join(w2)         # <-- ehrbrsw + ''.join([]) + ''.join([a,p]) = ehrbrswap

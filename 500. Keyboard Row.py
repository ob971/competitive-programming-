class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        res = []
        for i in words:
            j = set(i.lower())
            if j.issubset(s1) or j.issubset(s2) or j.issubset(s3):
                res.append(i)
        return res

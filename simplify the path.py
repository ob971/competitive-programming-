class Solution:
    def simplifyPath(self, path: str) -> str:
        return '/'+'/'.join(reduce(lambda r,p:((r+[p],r)[p in {'.',''}],r[:-1])[p=='..'],path.split('/'),[]))

ass Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        for key, group in groupby(chars):
            #print(k, list(g))
            count = len(list(group))
            s.append(key)
            if count > 1: s.extend(list(str(count)))
        chars[:] = s
         

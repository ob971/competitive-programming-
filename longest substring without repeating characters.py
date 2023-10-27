lass Solution(object):
    def lengthOfLongestSubstring(self, s):
        i, j, longest = 0, 0, 0
        charCount = {}

            
        while j < len(s):
            char = s[j]

            
            if char in charCount:
                i = max(i, charCount[char] + 1)

            
            charCount[char] = j
            longest = max(longest, j - i + 1)

            j += 1

        
        return longest

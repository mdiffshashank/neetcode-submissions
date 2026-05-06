class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1, l2 = 0, 0
        max_length = 0
        l = len(s)
        seen = set()

        while (l1 < l):
            if(s[l1] not in seen):
                seen.add(s[l1])
                l1 += 1
                length = l1 - l2
                max_length = max(length,max_length)
            else:
                seen.remove(s[l2])
                l2 += 1
        return max_length
        
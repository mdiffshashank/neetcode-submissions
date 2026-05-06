class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for s in strs:
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i])-ord('a')] += 1
            
            key = tuple(arr)

            if key in freq:
                freq.get(key).append(s)
            else:
                freq[key] = [s]

        return list(freq.values())

        
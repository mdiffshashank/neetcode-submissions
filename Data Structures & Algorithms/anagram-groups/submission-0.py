class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        result = []
        for s in strs:
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] += 1
            key = tuple(arr)
            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]
        
        return list(anagram_map.values())


        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        last_index = len(a) - 1
        last_string = a[last_index]
        return len(last_string)


        
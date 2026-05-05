class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = nums[:]
        for num in nums:
           ans.append(num)
        return ans
        
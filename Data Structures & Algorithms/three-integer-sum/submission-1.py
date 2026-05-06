class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] == nums[i-1] and i>0:
                continue

            l, r = i+1 , n-1
            while l < r:
                _3_sum = nums[i] + nums[l] + nums[r]
                if _3_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif _3_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res;


        
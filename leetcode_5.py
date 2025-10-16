# House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(houses):
            prev_max = 0
            curr_max = 0

            for money in houses:
                temp = curr_max
                curr_max = max(curr_max, prev_max + money)
                prev_max = temp

            return curr_max

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

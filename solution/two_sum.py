class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
                diff = target - num
                if diff in nums and nums.index(diff) != i:
                    break
        j = nums.index(diff)
        return [i, j]
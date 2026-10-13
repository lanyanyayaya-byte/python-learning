class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seed = {}
        for i in range(len(nums)):
            num = nums[i]
            need = target - num
            if need in seed:
                return [seed[need], i]
            seed[num] = i

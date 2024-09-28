class Solution:
    def inefficientTwoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return i, j


    def twoSum(self, nums: list[int], target: int) -> list[int]:
        coordinate_map = {nums[i]: i for i in range(len(nums))}
        for num in coordinate_map:
            try:
                pair = coordinate_map[target-num]
            except KeyError:
                continue
            else:
                return coordinate_map[num], coordinate_map[target-num]
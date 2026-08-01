class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for value, index in enumerate(nums):
            comp = target - index
            if comp in num_map:
                return [num_map[comp], value]
            num_map[index] = value

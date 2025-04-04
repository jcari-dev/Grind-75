from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement not in num_to_index:
                num_to_index[num] = index
            else:
                return (index, num_to_index[complement])
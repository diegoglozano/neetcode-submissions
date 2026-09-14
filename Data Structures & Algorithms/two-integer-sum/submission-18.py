class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) / O(n)
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[num] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hmap= {}

        for i , v in enumerate(nums):
            temp = target - v
            if temp in Hmap:
                return [Hmap[temp], i]
            else:
                Hmap[v] = i

        
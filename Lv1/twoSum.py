class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in (range(len(nums))):
                if (j!=i) and (nums[i] + nums[j] == target):
                    return [i,j]


a = Solution()
a.twoSum([1,2,3],5)
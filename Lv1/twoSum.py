# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in (range(len(nums))):
#                 if (j!=i) and (nums[i] + nums[j] == target):
#                     return [i,j]
#
#
# a = Solution()
# a.twoSum([1,2,3],5)

'''
투포인터란? 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽포인터를 오른쪽으로 옮기면서 값을 조정하는 방식이다.
'''

# def twopoint_twosum(nums,target):
#     left, right = 0, len(nums)-1
#     nums.sort()
#     while not left == right:
#         if nums[left] + nums[right] > target:
#             right -= 1
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             return left, right
#
# print(twopoint_twosum([2,3,1,1,2],2))

# 조회 구조 개선
def twoSum_sol3(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return nums_dict[target - num], i
        nums_dict[num] = i
print(twoSum_sol3([2,3,1,1,2],2))
##################################################################################
#
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
#
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are
# not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
# following things:
#
#   - Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
#     The remaining elements of nums are not important as well as the size of nums.
#   - Return k.
#
# Example 1:
#   Input: nums = [3,2,2,3], val = 3
#   Output: 2, nums = [2,2,_,_]
#   Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#                It does not matter what you leave beyond the returned k (hence they are underscores).
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
#
# Example 2:
#   Output: 5, nums = [0,1,4,0,3,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
#                Note that the five elements can be returned in any order.
#                It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
#   0 <= nums.length <= 100
#   0 <= nums[i] <= 50
#   0 <= val <= 100
##################################################################################
from typing import List


# INPUT
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


# SOLUTION
def remove_element(nums: List[int], val: int) -> int:
    # The following won't work because we would change the size of nums in-place,
    # which results in "index out of range" error when the loop
    # reaches an index greater than the current length of nums.
    # the length of nums
    # for i in range(len(nums)):
    #     if nums[i] is val:
    #         nums.pop(i)
    #
    # The for-loop below is iterating through every original element of nums,
    # and every element that is not equal to val is being overwritten in-place.
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# TIME COMPLEXITY OF SOLUTION
#   O(n)
#       - The algorithm iterates through each element of nums exactly once.
#       - The operation inside the loop is a simple conditional check and assignment,
#         both of which are O(1) operations.
#       - Therefore, the total time complexity is O(n), where n is the length of nums.
#
# Time Complexity
#   |             O(n)
#   |            *
#   |          *
#   |        *
#   |      *
#   |    *
#   |  *
#   |*
#   |------------------->
#       Input Size

# SPACE COMPLEXITY OF SOLUTION
#   O(1)
#       - The space complexity is constant because the modification is done in-place.
#       - The variable 'k' is the only additional storage used, which does not scale with
#         the size of the input list, nums.
#       - If we modified a copy of nums instead, the space complexity would be O(n),
#
# Space Complexity
#   |
#   |
#   |
#   |
#   |
#   |
#   |************************  O(1)
#   |
#   |------------------------->
#       Input Size


# TERMINAL OUTPUT
original_nums = nums.copy()
result = remove_element(nums=nums, val=val)
print(
    f"\nInput: nums = {original_nums}, val = {val}\nOutput: k = {result}, nums = {nums}\n"
)

# RUN COMMAND:
#   python array-string/remove_element.py

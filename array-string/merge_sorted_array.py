##################################################################################
#
# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
# integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside
# the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
# denote the elements that should be merged, and the last n elements are set to 0 and should be
# ignored. nums2 has a length of n.
#
# Example 1:
#   Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#   Output: [1,2,2,3,5,6]
#   Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#   The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
#   Input: nums1 = [1], m = 1, nums2 = [], n = 0
#   Output: [1]
#   Explanation: The arrays we are merging are [1] and [].
#   The result of the merge is [1].
#
# Example 3:
#   Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#   Output: [1]
#   Explanation: The arrays we are merging are [] and [1].
#   The result of the merge is [1].
#   Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure
#   the merge result can fit in nums1.
#
# Constraints:
#   nums1.length == m + n
#   nums2.length == n
#   0 <= m, n <= 200
#   1 <= m + n <= 200
#   -109 <= nums1[i], nums2[j] <= 109
##################################################################################
from typing import List


# INPUT
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3


# SOLUTION 1: Brute Force Method Using Insertion
def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # 1. Set initial indexes (last element of each)
    nums1_index = (m + n) - 1
    nums2_index = n - 1

    # 2. Merge nums2 into nums1 starting from the end
    while nums1_index >= 0 and nums2_index >= 0:
        nums1[nums1_index] = nums2[nums2_index]
        nums1_index -= 1
        nums2_index -= 1

    # 3. Sort nums1 using an insertion sorting algorithm.
    for i in range(1, m + n):
        temp = nums1[i]  # Index of current element to be sorted
        j = i - 1  # Index of element to the left of temp

        # If element to the left of temp is greater than temp, move temp to the left.
        # Repeat until the correct position of temp is found.
        while j >= 0 and temp < nums1[j]:
            nums1[j + 1] = nums1[j]
            j -= 1

        # Insert temp into the correct position.
        nums1[j + 1] = temp

    return nums1


# TIME COMPLEXITY OF SOLUTION 1
#   O(n^2)
#       - The merging of nums2 into nums1 takes O(n) time.
#       - The insertion sort algorithm used for sorting has a worst-case time complexity of O((m+n)^2),
#         where m and n are the lengths of nums1 and nums2 respectively.
#       - Therefore, the overall time complexity is dominated by the sorting step, which
#         in is O(n^2) in the general form (not relating to n in the problem above).
#
# Time Complexity
#   |                   O(n^2)
#   |                *
#   |               *
#   |             *
#   |           *
#   |        *
#   |    *
#   |*
#   |------------------------->
#       Input Size

# SPACE COMPLEXITY OF SOLUTION 1
#   O(1)
#       - The space complexity is constant because the sorting is done in place.
#       - No additional data structures are used that grow with the size of the input.
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


# SOLUTION 2: Simple Pythonic Solution
def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # 1. Replace the n elements of nums1 with the n elements of nums2
    nums1[n:] = nums2

    # 2. Use the built-in sort() method
    nums1.sort()

    return nums1


# TIME COMPLEXITY OF SOLUTION 2
#   O(n log n)
#       - The time complexity of Python's built-in sort() method is O(k log k),
#         where k is the length of the array. Here, k = m + n.
#       - Thus, the time complexity of sorting nums1 after merging nums2 into it is
#         O((m+n) log (m+n)), which in the general form is O(n log n).
#
# Time Complexity
#   |                    O(n log n)
#   |                  *
#   |                *
#   |              *
#   |           *
#   |        *
#   |    *
#   |*
#   |------------------------->
#       Input Size
#
# SPACE COMPLEXITY OF SOLUTION 2
#   O(1) or O(n)
#       - The space complexity is O(1) considering the in-place modification of nums1.
#       - However, under the hood, Python's sort() may use additional space (up to O(n)),
#         depending on the Python implementation and the sorting algorithm used.
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
#
# OR
#
# Space Complexity
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

# TERMINAL OUTPUT
result = merge1(nums1=nums1, m=m, nums2=nums2, n=n)
print(f"\nnums1: {nums1}\nm: {m}\nnums2: {nums2}\nn: {n}\nOutput: {result}\n")

# RUN COMMAND:
#   python array-string/merge_sorted_array.py

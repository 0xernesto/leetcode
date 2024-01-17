##################################################################################
#
# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
#
# You are given a large integer represented as an integer array digits, where each digits[i]
# is the ith digit of the integer. The digits are ordered from most significant to least
# significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
#
# Example 1:
#   Input: digits = [1,2,3]
#   Output: [1,2,4]
#   Explanation: The array represents the integer 123.
#   Incrementing by one gives 123 + 1 = 124.
#   Thus, the result should be [1,2,4].
#
# Example 2:
#   Input: digits = [4,3,2,1]
#   Output: [4,3,2,2]
#   Explanation: The array represents the integer 4321.
#   Incrementing by one gives 4321 + 1 = 4322.
#   Thus, the result should be [4,3,2,2].
#
# Example 3:
#   Input: digits = [9]
#   Output: [1,0]
#   Explanation: The array represents the integer 9.
#   Incrementing by one gives 9 + 1 = 10.
#   Thus, the result should be [1,0].
#
# Constraints:
#   1 <= digits.length <= 100
#   0 <= digits[i] <= 9
#   digits does not contain any leading 0's
##################################################################################
from typing import List


# INPUT
digits = [1, 2, 9]


# SOLUTION
def plus_one(digits: List[int]) -> List[int]:
    # Convert digits array to a number string
    integer_string = ""
    for digit in digits:
        integer_string += str(digit)

    # Cast number string to in and add one
    integer_plus_one = int(integer_string) + 1

    # Reassemble int array
    new_digits_array = []
    for digit in str(integer_plus_one):
        new_digits_array.append(int(digit))

    return new_digits_array


# TIME COMPLEXITY OF SOLUTION
#   O(n)
#       - The first loop concatenates each digit in the input list into a string,
#         resulting in a linear time complexity proportional to the length of the list (n).
#       - The integer conversion, addition, and conversion back to a string are all O(n) operations,
#         as they depend on the length of the string.
#       - The second loop iterates over the string representation of the integer and converts
#         each character back to an integer, which again results in a linear time complexity
#         proportional to the number of digits in the integer.
#       - Overall, each step is linear with respect to the number of digits in the input list,
#         leading to an overall time complexity of O(n).

# SPACE COMPLEXITY OF SOLUTION
#   O(n)
#       - The space complexity is also linear (O(n)) due to the storage requirements of the
#         'integer_string' and 'new_digits_array'.
#       - The 'integer_string' grows linearly with the number of digits in the input list.
#       - Similarly, the 'new_digits_array' is proportional in size to the number of digits
#         in the modified number.
#       - Thus, the space complexity is linear with respect to the number of digits in the input list.


# Complexity
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
result = plus_one(digits)
print(f"\nInput: {digits}\nOutput: {result}\n")

# RUN COMMAND:
#   python math/plus_one.py

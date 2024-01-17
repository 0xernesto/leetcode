##################################################################################
#
# https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
#
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#   - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
# Example 1:
#   Input: x = 4
#   Output: 2
#   Explanation: The square root of 4 is 2, so we return 2.
#
# Example 2:
#   Input: x = 8
#   Output: 2
#   Explanation: The square root of 8 is 2.82842..., and since we round
#                it down to the nearest integer, 2 is returned.
#
# Constraints:
#   0 <= x <= 231 - 1
##################################################################################

# INPUT
x = 500


# SOLUTION 1: Brute Force Method
def sqrt_x_1(x: int) -> int:
    # The square root of 0 or 1 is the number itself
    if x == 0 or x == 1:
        return x

    # Create array of integers up to x
    test_array = []
    for i in range(0, x + 1):
        test_array.append(i)

    # Brute Force Method
    for i in test_array:
        if i * i > x:
            return i - 1


# TIME COMPLEXITY OF SOLUTION 1
#   O(n)
#       - The creation of 'test_array' with a range of integers from 0 to x takes O(n) time.
#       - The subsequent loop to find the square root also takes O(n) time in the worst case, as it
#         iterates over 'test_array' which has a length proportional to x.
#       - Therefore, the overall time complexity is O(n) + O(n) which simplifies to O(n).

# SPACE COMPLEXITY OF SOLUTION 1
#   O(n)
#       - The space complexity is O(n) due to the size of 'test_array', which stores n+1 integers.
#       - No additional space that grows with the input size is allocated.

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


# SOLUTION 2: Binary Search Method
def sqrt_x_2(x: int) -> int:
    # The square root of 0 or 1 is the number itself
    if x == 0 or x == 1:
        return x

    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


# TIME COMPLEXITY OF SOLUTION 2
#   O(log n)
#       - The algorithm uses a binary search approach, which cuts the search space in half
#         with each iteration.
#       - This results in a time complexity of O(log n), which means the time complexity growth
#         rate slows as the input size grows.
#
# Time Complexity
#   |
#   |
#   |
#   |                **********  O(log n)
#   |         *******
#   |    ****
#   | **
#   |*
#   |------------------------->
#       Input Size

# SPACE COMPLEXITY OF SOLUTION 2
#   O(1)
#       - The space complexity is constant because the algorithm uses a fixed number of
#         variables (left, right, mid, mid_squared) and does not allocate any additional
#         space that grows with the size of the input.
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


# SOLUTION 3: Newton Method
def sqrt_x_3(x: int) -> int:
    # The square root of 0 or 1 is the number itself
    if x == 0 or x == 1:
        return x

    # Newton's Method
    #   - Need to find a number r such that r^2 = x
    #       - Mathematically, we are looking for the root of r^2 - x = 0
    #   - We can use the derivative of f(r) to find the root of a line tangent to f(r)
    #   - The derivative of f(r) = r^2 - x is f'(r) = 2r
    #   - Using the point-slope formula, the equation of the tangent line is
    #     y = f'(r)(x - r) + f(r)
    #   - Setting y = 0 in the tangent line equation (finding the x-intercept) gives:
    #     0 = 2r(x - r) + (r^2 - x)
    #   - Simplifying, we find the next approximation: r_new = (r_old + x / r_old) / 2
    #   - Each iteration updates r to a better approximation of the square root of x
    r = x
    while r * r > x:
        r = (r + (x // r)) // 2
    return r


# TIME COMPLEXITY OF SOLUTION 3
#   O(log n)
#       - Newton's Method converges quadratically close to the root, which often means
#         it requires fewer iterations than binary search.
#       - However, each iteration involves a division and addition, which are constant-time
#         operations. Thus, the overall time complexity remains logarithmic with respect to
#         the input size, similar to binary search but typically with a smaller constant factor.
#
# Time Complexity
#   |
#   |
#   |
#   |                **********  O(log n)
#   |         *******
#   |    ****
#   | **
#   |*
#   |------------------------->
#       Input Size

# SPACE COMPLEXITY OF SOLUTION 3
#   O(1)
#       - Space complexity is constant as the algorithm uses a single additional variable 'r'
#         for its computations, irrespective of the size of 'x'.
#       - No additional data structures or recursive calls that would require extra space are used.
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
result = sqrt_x_3(x)
print(f"\nInput: {x}\nOutput: {result}\n")

# RUN COMMAND:
#   python math/sqrt_x.py

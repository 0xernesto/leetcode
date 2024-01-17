##################################################################################
#
# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#   Input: s = "()"
#   Output: true
#
# Example 2:
#   Input: s = "()[]{}"
#   Output: true
#
# Example 3:
#   Input: s = "(]"
#   Output: false
#
#
# Constraints:
#   1 <= s.length <= 104
#   s consists of parentheses only '()[]{}'.
##################################################################################

# INPUT
input_string = "()[{}]"


# SOLUTION
def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False
            top_element = stack.pop()
            if char == ")" and top_element != "(":
                return False
            if char == "]" and top_element != "[":
                return False
            if char == "}" and top_element != "{":
                return False

    # if the for-loop finished executing, all brackets were matched
    # correctly, the stack should be empty, and we can now return true.
    if len(stack) == 0:
        return True


# TIME COMPLEXITY OF SOLUTION
#   O(n)
#       - The algorithm iterates through each character of the string s once.
#       - Each iteration involves constant-time operations (checking and
#         pushing/popping from the stack).
#       - Hence, the time complexity is linear with respect to the length of the
#         input string s.

# SPACE COMPLEXITY OF SOLUTION
#   O(n)
#       - In the worst case, all characters in the string are opening brackets,
#         leading to all of them being pushed onto the stack.
#       - Therefore, the maximum stack size could be equal to the length of the string s.
#       - Thus, the space complexity is linear with respect to the length of the input string s.

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
result = is_valid(input_string)
print(f'\nInput String: "{input_string}"\nValid Parentheses: {result}\n')


# RUN COMMAND:
#   python stack/valid_parentheses.py

##################################################################################
#
# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
#
# Given two strings ransom_note and magazine, return true if ransom_note can
# be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransom_note.
#
# Example 1:
#   Input: ransom_note = "a", magazine = "b"
#   Output: false
#
# Example 2:
#   Input: ransom_note = "aa", magazine = "ab"
#   Output: false
#
# Example 3:
#   Input: ransom_note = "aa", magazine = "aab"
#   Output: true
#
# Constraints:
#   1 <= ransom_note.length, magazine.length <= 105
#   ransom_note and magazine consist of lowercase English avail_letters.
##################################################################################

# INPUT
ransom_note = "hello world"
magazine = "The old wheel rolls."


# SOLUTION
def can_construct(ransom_note: str, magazine: str) -> bool:
    # 1. Construct a dict where the key is a letter and the value
    #    is the amount of times this letter appears in the magazine.
    avail_letters = {}
    for letter in magazine:
        if letter in avail_letters:
            avail_letters[letter] += 1
        else:
            avail_letters[letter] = 1

    # 2. Check if each letter in ransom_note is in avail_letters and
    #    if we have at least 1 of this letter available.
    #    If the loop finishes executing without returning False, the
    #    ransom_note can be constructed from avail_letters.
    for letter in ransom_note:
        if letter in avail_letters:
            if avail_letters[letter] > 0:
                avail_letters[letter] -= 1
            else:
                return False
        else:
            return False

    return True


# TIME COMPLEXITY OF SOLUTION
#   O(n)
#       - The algorithm first iterates through each letter in the magazine (length m),
#         adding to or creating a key in the avail_letters dict.
#       - It then iterates through each letter in the ransom_note (length k).
#       - Hence, the total time complexity is O(m) for the magazine loop plus O(k) for the
#         ransom_note loop, resulting in O(m + k), which in general form condenses down to O(n).
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
#
# SPACE COMPLEXITY OF SOLUTION
#   O(1)
#       - Since the amount of unique characters in the magazine is limited, the
#         avail_letters dict will not grow indefinitely.
#       - Hence, the space complexity is O(1) .
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
result = can_construct(ransom_note=ransom_note, magazine=magazine)
print(
    f'\nInput: ransom_note="{ransom_note}", magazine="{magazine}"\nOutput: {result}\n'
)


# RUN COMMAND:
#   python hashmap/ransom_note.py

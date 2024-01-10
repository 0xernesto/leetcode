##################################################################################
#
# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
#
# Given head, the head of a linked list, determine if the linked list has a cycle
# in it.
#
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Internally, pos is used
# to denote the index of the node that tail's next pointer is connected to. Note that
# pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Constraints:
#   The number of the nodes in the list is in the range [0, 104].
#   -105 <= Node.val <= 105
#   pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
##################################################################################

# SETUP
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# INPUT
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle


# SOLUTION
def has_cycle(head: Optional[ListNode]) -> bool:
    visited_nodes = set()
    current_node = head
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)
        current_node = current_node.next
    return False


# TIME COMPLEXITY OF SOLUTION
#   O(n)
#       - The algorithm iterates through each node in the linked list once.
#       - Each iteration involves checking if a node is in the set and adding the
#         node to the set, both constant-time operations.
#       - Hence, the time complexity is linear with respect to the number of nodes
#         in the linked list.

# SPACE COMPLEXITY OF SOLUTION
#   O(n)
#       - In the worst case, every node in the linked list is added to the 'visited_nodes' set.
#       - Therefore, the maximum size of the 'visited_nodes' set could be equal to the number
#         of nodes in the linked list.
#       - Thus, the space complexity is linear with respect to the number of nodes in the linked list.

# Complexity
#   |             O(n)
#   |            .
#   |          .
#   |        .
#   |      .
#   |    .
#   |  .
#   |.
#   |------------------->
#       Input Size


# TERMINAL OUTPUT
input_head = node1
result = has_cycle(input_head)
print(
    f"\nInput Linked List Values: [{node1.val}, {node2.val}, {node3.val}, {node4.val}]\nCycle: {result}\n"
)

# RUN COMMAND:
#   python linked-list/linked_list_cycle.py

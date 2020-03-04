# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node, curr_node = None, head
        # sets prev_node to null, curr_node now points to head
        while curr_node:
            curr_node.next, prev_node, curr_node = prev_node, curr_node, curr_node.next
            # curr_node.next points to null on first round, then prev_node on next iterations
            # prev_node is now curr_node
            # curr_node now points to next node, curr_node.next is not
            # pointing prev_node yet because it was all done in one line
        return prev_node

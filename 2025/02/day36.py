# Leetle Day 36 - Single Linked List Middle
# 05.02.2025

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
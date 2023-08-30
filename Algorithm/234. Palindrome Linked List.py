# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        # O space > 1
        s = ''
        while head:
            s += str(head.val)
            head = head.next

        return s == s[::-1]
        '''
        slow = fast = prev = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow
        fast = head
        slow = prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next

        return True
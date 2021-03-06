# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
        	tmp = head.next
        	head.next = pre
        	pre = head
        	head = tmp
        return pre

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return head
        next = head.next
        head.next = None
        if next:
        	tmp = self.reverseList(next)
        	next.next = head
        	return tmp
        return head
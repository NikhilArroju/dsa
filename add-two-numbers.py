from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = ListNode()
        finalNode = resultNode
        # print(l1)
        flag = True
        carry = 0
        while flag:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            if l1 == None and l2 == None:
                flag = False
            sum += carry
            if sum > 9:
                resultNode.val = sum-10
                carry = 1
                # print(resultNode.val)
            else:
                resultNode.val = sum
                carry = 0
                # print(resultNode.val)
            resultNode.next = ListNode() if flag or carry > 0 else None
            resultNode = resultNode.next
        if carry > 0:
            resultNode.val = carry
        return finalNode

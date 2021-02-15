# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# method 0: 포인터 조절 > 40 ms	14.3 MB
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_head = None
        res = None

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                if res == None:
                    res_head = res = l1
                    l1 = l1.next
                else:
                    res.next = l1
                    l1 = l1.next
                    res = res.next
            else:
                if res == None:
                    res_head = res = l2
                    l2 = l2.next
                else:
                    res.next = l2
                    l2 = l2.next
                    res = res.next

        if l1 != None:
            res.next = l1
        if l2 != None:
            res.next = l2

        return res_head

# method 1: 재귀 구조 > 36 ms	14.4 MB
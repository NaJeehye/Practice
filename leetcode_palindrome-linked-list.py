# https://leetcode.com/problems/palindrome-linked-list/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# method 0: 리스트 사용 > 68 ms	24.1 MB

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. 리스트에 val 투입
        ing = head
        val_list = []

        while ing != None:
            val_list.append(ing.val)
            ing = ing.next

        # 2. 펠린드롬 방법을 사용한다.
        if len(val_list) == 0:
            return True
        for i in range(len(val_list) // 2):
            if val_list[i] != val_list[-i - 1]:
                return False
        return True

# method 1: 데크를 이용한 최적화 >	72 ms	24.1 MB
# 파이썬의 테크는 이중 연결 리스트 쿠조로 양쪽 방향의 모두 추출하는데 시간 복잡도 1이 소요됨
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

#[올바른풀이법]method 2: 런너를 이용한 풀이 > 60 ms	24.3 MB
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        # 팰린드롬 여부확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
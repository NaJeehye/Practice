# https://leetcode.com/problems/reverse-string/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# method 0 : two pointer swap : 196 ms	18.8 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s=len(s)
        for i in range(int(len_s/2)):
            char=s[i]
            s[i]=s[-i-1]
            s[-i-1]=char

# method 1 : Using built-in function 196 ms	18.6 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
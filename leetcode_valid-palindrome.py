# https://leetcode.com/problems/valid-palindrome/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# method 0 : Using String : 40 ms	14.4 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # refine unnecessary words
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char

        clean_s = clean_s.lower()
        len_s = len(clean_s)

        if clean_s == "":
            return True

        # we don't consider whether the number is even or odd.
        for i in range(int(len_s / 2)):
            if clean_s[i] != clean_s[-i - 1]:
                return False
        return True

# method 1: Using List : 284 ms	19.4 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.pop(0)!=strs.pop():
                return False
        return True

# method 2 : Using Deque : 48 ms	19.4 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs : Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.popleft()!=strs.pop():
                return False
        return True

# method 3 : Using Slicing : 36 ms	15.8 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)
        return s == s[::-1] # Slicing
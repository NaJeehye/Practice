# https://leetcode.com/problems/longest-palindromic-substring/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# method 0 : Using String : 3264 ms	14.3 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.lower()
        # s=re.sub('[^a-z0-9]','',s)
        return s == s[::-1]  # Slicing

    def longestPalindrome(self, s: str) -> str:
        curr_len = 0
        best_len = 0
        best_pal = ""

        start_idx = 0
        end_idx = len(s)

        for idx, center in enumerate(s):
            curr_pal = center
            left = idx
            right = idx + 1  # consider removed elements
            is_changed = True

            while left >= start_idx and right <= end_idx and is_changed == True:
                is_changed = False

                # increase right
                right += 1
                if right <= end_idx and self.isPalindrome(s[left:right]):
                    curr_pal = s[left:right]
                    is_changed = True

                # increase left
                left -= 1
                if left >= start_idx and self.isPalindrome(s[left:right]):
                    curr_pal = s[left:right]
                    is_changed = True

            if len(curr_pal) > best_len:  # curr_len>best_len
                best_pal = curr_pal  # best_pal=curr_pal
                best_len = len(curr_pal)

        return best_pal

# Method 1: 중앙을 중심으로 확장하는 풀이 : 272 ms	14.5 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result
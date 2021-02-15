# https://leetcode.com/problems/product-of-array-except-self/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함
# Medium

# Method 0: left/right ==> Time Limit Exceeded
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        output=[]
        for i in range(length):
            if i==0:
                left=1
            else:
                left=left*nums[i-1]
            right=1
            if i!=(length-1):
                for n in nums[i+1:]:
                    right=right*n
            output.append(left*right)
        return output

# Method 1: 왼쪽 곱셈결과에 오른쪽 값을 차례대로 곱셈 : 228 ms	21 MB
## 자신을 제외하고 왼쪽의 곱셈 결과와 온른쪽의 곱셈 결과를 곱해야한다.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        p=1
        # 왼쪽 곱셈
        for i in range(0,len(nums)):
            out.append(p)
            p=p*nums[i]
        p=1
        #왼쪽과 오른쪽 곱셈 결과에 오른쪽 값을 차례로 곱셈
        for i in range(len(nums)-1,0-1,-1):
            out[i]=out[i]*p
            p=p*nums[i]
        return ou
# https://leetcode.com/problems/3sum/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# [caution] No 브루트 포스
# Method 1 : 브루트 포스 --> Time Limit Exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        result=[]
        # [문제 풀기전 think] nums에서 value만 사용하고, index는 고려사항 X
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: # don't consider duplication
                continue
            for j in range(i+1,len(nums)-1):
                if j>(i+1) and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,len(nums)):
                    if k>(k+1) and nums[k]==nums[k-1]:
                        continue
                    if nums[i]+nums[j]+nums[k]==0:
                        result.append([nums[i],nums[j],nums[k]])
                        break
        return result

# Method 2: 투 포인터 합 계산 848 ms	17.3 MB
# ==> O(n^2)로 위의 해결책보다 시간 복잡도가 월등히 낮음
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = []
        # [문제 풀기전 think] nums에서 value만 사용하고, index는 고려사항 X
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # don't consider duplication
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res < 0:
                    left += 1  # need to increase
                elif res > 0:
                    right -= 1  # need to decrease
                else:
                    # sum=0인 경우 정답 및 스킵 처리
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        # left가 새로운 값을 얻기 전 까지
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # right가 새로운 값을 얻기 전까지
                        right -= 1
                    # 새로운 값으로 업데이트
                    left += 1
                    right -= 1
        return result

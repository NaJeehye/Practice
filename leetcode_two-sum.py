# https://leetcode.com/problems/two-sum/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Method 0 : Using Brute-Force(무차별 대입 방식) : 36 ms	14.4 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1 in range(0,len(nums)-1):
            for idx2 in range(idx1+1,len(nums)):
                if nums[idx1]+nums[idx2]==target:
                    return [idx1,idx2]

# Method 1 : "in"을 이용한 탐색 : 48 ms	14.5 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            complement=target -n
            if complement in nums[i+1:]:ㄴ
                return nums.index(n),nums[i+1:].index(complement)+(i+1)

# Method 2 : 첫번째 수를 뺀 결과 키 조회(Method 1개선 -> 한번에 정답찾기): 44 ms	14.6 MB
# [제약 조건이 없었다면, 에러가 뜰 수 있는 다양한 경우가 존재함]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫번째수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]

# Method 3 : 조회 구조 개선 :	48 ms	14.5 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={} # 앞서 봤던 것들이 저장되어 있을 것임
        # 하나의 for 문으로 통합
        for i,num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i

# Method 4 : 투 포인터 이용 => 풀이불가
# [sorted된 nums가 아니기 때문에 불가능하다, 만약 sort를 하면, 인덱스가 엉망이 되기 때문에 심각한 문제 발생]
# sorted가 가정이 되었다면, 해당 풀이 방법을 통한다면, 가장 빠르게 문제를 풀 수 있을 것이다.
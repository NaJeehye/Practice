# https://leetcode.com/problems/array-partition-i/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Method 0 : sorting -> 짝수값 개산: 268 ms	16.8 MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 어떤식으로 pairwise할거냐에 따라서 다르다.

        ## [문제 풀기전 think] nums에서 value만 사용하고, index는 고려사항 X
        nums.sort()

        output = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                output += nums[i]
        return output

# Method 1: 오름차순 풀이 : 296 ms	16.7 MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 어떤식으로 pairwise할거냐에 따라서 다르다.

        output = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계싼
            pair.append(n)
            if len(pair) == 2:
                output += min(pair)
                pair = []

        return output

# Method 2: 파이썬 다운 풀이 : 256 ms	16.9 MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 어떤식으로 pairwise할거냐에 따라서 다르다.
        return sum(sorted(nums)[::2])
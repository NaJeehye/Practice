# https://leetcode.com/problems/reorder-data-in-log-files/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Method 0 : using lambda : 40 ms	14.2 MB
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_log = []  # let_id let_logs
        dig_log = []  # dig_id dig_logs

        # enter
        for log in logs:
            if log.split(" ")[1].isdigit():
                dig_log.append(log)
            else:
                let_log.append(log)

        # sorting let_log
        let_log.sort(
            key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))  # sorting by using str[1:] and str[0] one by one.

        solution = []

        while let_log:
            solution.append(let_log.pop(0))
        while dig_log:
            solution.append(dig_log.pop(0))

        return solution

# Method 1 : Using lambda AND + operator : 40 ms	14.5 MB
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_log = []  # let_id let_logs
        dig_log = []  # dig_id dig_logs

        # enter
        for log in logs:
            if log.split(" ")[1].isdigit():
                dig_log.append(log)
            else:
                let_log.append(log)

        # sorting let_log
        let_log.sort(
            key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))  # sorting by using str[1:] and str[0] one by one.

        return let_log + dig_log
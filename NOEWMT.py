class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        NOEWMT = 0
        for x in range(len(hours)):
            if hours[x] >= target:
                NOEWMT += 1

        return NOEWMT

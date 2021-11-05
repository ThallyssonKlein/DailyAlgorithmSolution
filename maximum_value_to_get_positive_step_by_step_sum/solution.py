class Solution:
    def __init__(self):
        self.initialValue = 1
        self.solved = False

    def minStartValue(self, nums: List[int]) -> int:
        lastSumResult = self.initialValue
        wrong = False
        for num in nums:
            lastSumResult = lastSumResult + num
            if lastSumResult < 1:
                self.initialValue += 1
                wrong = True
                break
        if wrong:   
            self.minStartValue(nums)
            if self.solved:
                return self.initialValue
        else:
            self.solved = True
            return self.initialValue
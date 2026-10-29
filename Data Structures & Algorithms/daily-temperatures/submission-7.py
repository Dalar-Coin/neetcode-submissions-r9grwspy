class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        counter = []

        for i in range(len(temperatures)):
            while counter and temperatures[i] > counter[-1][0]:
                counterT, counterInd = counter.pop()
                result[counterInd] = i - counterInd
            counter.append((temperatures[i], i))
        return result
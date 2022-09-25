class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, num1 in enumerate(arr):
            for m, num2 in enumerate(arr):
                if num1 * 2 == num2 and i != m:
                    return True
        return False
        
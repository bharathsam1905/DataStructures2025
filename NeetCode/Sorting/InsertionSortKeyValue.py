# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}, {self.value})"
    '''

`__repr__` is a special method that defines **how your object looks when printed**. Now the output will look like:
'''

class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        n = len(pairs)
        res = []
        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            res.append(pairs[:])
        return res


s = Solution()
print(s.insertionSort([Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]))
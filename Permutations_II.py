# 加上一行查重，在遇到res[i]和num相同的情况，就跳出，不然就会出现[num, res[i], ...]和[res[i], num, ...]的重复情况
# nums = [1,2,2]
# num = 1, res = [], m = [[1]] = results;
# num = 2, res = [1], i = 0, m = [[2, 1]];
# num = 2, res = [1], i = 1, m = [[2, 1], [1, 2]] = results;
# num = 2, res = [2, 1], i = 0, res[i] = 2 = num, m = [[2, 2, 1]];
# num = 2, res = [1, 2], i = 0, m = [[2, 2, 1], [2, 1, 2]];
# num = 2, res = [1, 2], i = 1, res[i] = 2 = num, m = [[2, 2, 1], [2, 1, 2], [1, 2, 2]];
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            m = []
            for res in results:
                for i in range(len(res)+1):
                    m += [res[:i] + [num] + res[i:]]
                    if i < len(res) and res[i] == num:
                        break
            results = m
        return results

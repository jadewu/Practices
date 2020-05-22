# 沿用Subsets的模板：for num in nums; for res in results; 多加一个for i in range(len(res)+1)
# 例子：[1,2,3]
# num=1, res=[], i=0, m+=[res[:0]+[1]+res[0:]]=[[1]]=results
# num=2, res=[1], i=0, m+=[res[:0]+[2]+res[0:]]=[[2,1]];
# num=2, res=[1], i=1, m+=[res[:1]+[2]+res[1:]]=[[1,2]]; results=[[2,1], [1,2]]
# num=3, res=[2,1], i=0, m+=[res[:0]+[3]+res[0:]]=[[3,2,1]]
# num=3, res=[2,1], i=1, m+=[res[:1]+[3]+res[1:]]=[[2,3,1]]
# num=3, res=[2,1], i=2, m+=[res[:2]+[3]+res[2:]]=[[2,1,3]]
# num=3, res=[1,2], i=0, m+=[res[:0]+[3]+res[0:]]=[[3,1,2]]
# num=3, res=[1,2], i=1, m+=[res[:1]+[3]+res[1:]]=[[1,3,2]]
# num=3, res=[1,2], i=2, m+=[res[:2]+[3]+res[2:]]=[[1,2,3]]; results=[[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            m = []
            for res in results:
                for i in range(len(res)+1):
                    m += [res[:i] + [num] + res[i:]]
            results = m
            #print(results)
        return results

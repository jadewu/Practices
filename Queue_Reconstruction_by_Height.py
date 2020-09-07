# 这道题的意思是，每个人有一个数组(h, n)，h是身高，n是前面的比它高或者跟它一样高的人的个数，O(n^2)
# 对于所有n是0的人，应当从小到大排列，否则会出现矛盾，即n其实大于0的情况
# 对于所有n是k的人，也应当从小到大排列，因为如果i+1比i矮，那么前面比i+1高的人数应当比k多，起码是k+1
# 所以可以将数组按照h从大到小sort，n需要按照从小到大sort，因为相等h也会让n增加
# 把每一项插入到结果中，插入的位置就是n
# 因为是按照h从大到小插入的，所以对于每个人，经历插入操作之前，结果数列中前n个人，都会是比它高的
# 以后在插入比这个人矮的人的时候，就不会影响
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0], x[1]))
        # print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

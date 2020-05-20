# 一个比较简单巧妙的解法，two pointers + sliding window
class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        # need 用来存放t里各个letter和个数，missing指的是t里的元素还差多少个
        need = collections.Counter(t)
        # missing 指的是需求元素的总个数
        missing = len(t)
        # i是window的起始，I,J分别是作为结果的window的起始、终点
        i = I = J = 0
        
        # j是从1开始，c是从s的第一项开始
        for j, c in enumerate(s, 1):
            print(j,c)
            # 如果c在need里面而且是需求的状态
            if need[c] > 0:
                # 需求元素总个数减一
                missing -= 1
            # 每遍历一个char，就将need里对应的value-1，如果char是need里面本来没有的，那初始就是-1，不满足上面if的条件
            need[c] -= 1
            # 当t里面的所有元素都有了，开始重置
            if not missing:
                # 这个need[s[i]]<0代表了两种情况：
                # 这个字母并不在t里面所以也不需要在新的window里面
                # 这个字母在t里面，在原来的window里的i这个位置出现了一次，在i之后还会再出现一次或多次，所以i也是不需要再新的window里的
                while i < j and need[s[i]] < 0:
                    # 恢复s[i]对应的key在need里的value到新window的状态
                    need[s[i]] += 1
                    # 向右移动window的起始，即新window不需要s[i]
                    i += 1
                # 如果还没有记录J，或者新的window比之前的要短，则需要更新结果
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
    
    def found_target(target_len):
    return target_len == 0

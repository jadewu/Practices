# 把logs里的单词分成两个lists，分别是letters和digits
# letters先按照suffix排一遍，再按照内容排一遍；digits保持原本的顺序
# 把letters放在digits前面
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # when suffix is tie, sort by identifier        
        letters.sort(key = lambda x: x.split()[0])
        # sort by suffix
        letters.sort(key = lambda x: x.split()[1:])
        # put digits after letters
        result = letters + digits                                        
        return result

# Define sorted function for different types
# 如果是letters就标为0，如果是digits就标为1，在sorted的时候，0一定会在1之前，所以letters会放在digits前
# 其中，letters的顺序，先是按照每一个词的alphabet顺序排，然后再按suffix排；digits的顺序，就保持原来的
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            # 分成log[0]和log[0]之后的部分
            idx, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, idx)
            else:
                return (1,)
        return sorted(logs, key = f)

# 一行的做法, str.join(list/tuple, key function) key function用来排序
class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(" "), key=len)).capitalize()

# 自己的做法
class Solution:
    def arrangeWords(self, text: str) -> str:
        l = text.split(' ')
        print(l)
        d = {}
        for i in range(len(l)):
            d[i] = len(l[i])
        # print(d)
        
        # sorted(list, key=key function) 格式和上面的join()一样，
        # lambda item: item[1] is an inline function 等同于 def first(item): return item[1]
        sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        # print(sorted_d)
        res = ''
        f = 1
        for k, v in sorted_d.items():
            if f:
                res += l[k][0].upper()
                res += l[k][1:] + ' '
                f = 0
            else:
                res += l[k].lower() + ' '
        # print(res)
        return res[:-1]

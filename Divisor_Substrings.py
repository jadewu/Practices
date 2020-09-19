# 两个小写字母组成的字符串s1, s2，字符串内部可以换位，两个字母的出现频率可以互换，判断是否能把s1换成s2
# 所以只需要两个字符串的字母种类和出现频率一样就行
s1 = "babzccc"
s2 = "bbazzcz"
m = len(s1)
n = len(s2)
d1, d2 = {}, {}
if m == n:
    for i in range(m):
        if s1[i] not in d1:
            d1[s1[i]] = 1
        else:
            d1[s1[i]] += 1
        if s2[i] not in d2:
            d2[s2[i]] = 1
        else:
            d2[s2[i]] += 1
    print(d1, d2)
    v1, v2 = [], []
    flg = 1
    for k, v in d1.items():
        if k not in d2:
            flg = 0
            print("False")
            break
        v1.append(d1[k])
        v2.append(d2[k])
    if flg and sorted(v1) == sorted(v2):
        print("True")
    else:
        print("False")
else:
    print("False")

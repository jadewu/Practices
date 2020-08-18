# 购物车问题：https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tags=&title=&diffculty=0&judgeStatus=0&rp=1
# 是比较复杂的0/1背包问题：定义状态转移数组dp[i][j]，表示前i个物品，背包重量为j的情况下能装的最大价值。
# 先处理数据，把主件和分部件分开放，然后进行dp状态转移方程。
# 考虑每个物品时要考虑每种可能出现的情况，1、主件，2、主件+附件1，3、主件+附件2，4、主件+附件1+附件2，不一定每种情况都出现，只有当存在附件时才会出现对应的情况。
# dp[i][j] = max(物品不放入背包，主件，主件+附件1，主件+附件2，主件+附件1+附件2)
# 题解
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:#主件
        primary[i] = [x, y]
    else:#附件
        if z in annex:#第二个附件
            annex[z].append([x, y])
        else:#第一个附件
            annex[z] = [[x,y]]
m = len(primary)#主件个数转化为物品个数
dp = [[0]*(n+1) for _ in range(m+1)]
w, v= [[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])#1、主件
    v_temp.append(primary[key][0]*primary[key][1])
    if key in annex:#存在主件
        w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
        v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#存在两主件
            w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1,m+1):
    for j in range(10,n+1,10):#物品的价格是10的整数倍
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])

# 自己的做法
import sys
line1 = sys.stdin.readline().split()
n, m = int(line1[0]), int(line1[1])
d1, d2 = {}, {}
for j in range(1, m+1):
    linej = sys.stdin.readline().split()
    v, p, q = int(linej[0]), int(linej[1]), int(linej[2])
    if q == 0:
        d1[j] = [v, p]
    else:
        if q not in d2:
            d2[q] = [[v, p]]
        else:
            d2[q].append([v, p])
# print(d1, d2)

c = len(d1)
dp = [[0]*(n+1) for _ in range(c+1)]
# print(dp)
count = 0
for key, val in d1.items():
    count += 1
    for cur in range(1, n+1):
        if val[0] <= cur:
            cur_max = dp[count-1][cur-val[0]] + val[0]*val[1]
            if key in d2:
                if len(d2[key]) == 1:
                    a = d2[key][0]
                    if val[0] + a[0] <= cur:
                        cur_max = max(cur_max, dp[count-1][cur-val[0]-a[0]] + val[0]*val[1] + a[0]*a[1])
                else:
                    a, b = d2[key][0], d2[key][1]
                    if val[0] + a[0] <= cur:
                        cur_max = max(cur_max, dp[count-1][cur-val[0]-a[0]] + val[0]*val[1] + a[0]*a[1])
                    if val[0] + b[0] <= cur:
                        cur_max = max(cur_max, dp[count-1][cur-val[0]-b[0]] + val[0]*val[1] + b[0]*b[1])
                    if val[0] + a[0] + b[0] <= cur:
                        cur_max = max(cur_max, dp[count-1][cur-val[0]-b[0]-a[0]] + val[0]*val[1] + a[0]*a[1] + b[0]*b[1])
            dp[count][cur] = max(dp[count-1][cur], cur_max)
        else:
            dp[count][cur] = dp[count-1][cur]
        # print(dp)
print(dp[c][n])

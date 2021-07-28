# Construct palindromes with multiple inputs and multiple outputs

import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        l = list(line)
        m = len(l)
        re = []
        for j in l:
            re.append(j)

        re.reverse()

        dp = [[0 for j in range(m)] for i in range(m)]

        for i in range(m):
            for j in range(m):
                if l[i] == re[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(m - dp[m-1][m-1])

except:
    pass

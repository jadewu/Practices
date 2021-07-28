# 1. Two Sum

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                res = [d[target-nums[i]],i]
                return res
            d[nums[i]] = i

# 7. Reverse Integer (c++)
class Solution7 {
public:
    int reverse(int x) {
        string a = to_string(x);
        string res = "";
        if(a.find("-")!=string::npos){
            res += "-";
        }
        for(int i=a.length()-1;i>=0;i--){
            res += a.substr(i,1);
        }
        if(stoll(res) > 2147483647 || stoll(res) < -2147483648){
		return 0;
	    }
        return stoi(res);
    }
};

# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0
        n = x
        while n:
            r = 10*r + n%10
            n = int(n/10)
        if r==x:
            return True
        else:
            return False

13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if d[s[i+1]] > d[s[i]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        res += d[s[-1]]
        return res

14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs = sorted(strs)
        lens = []
        for i in strs:
            lens.append(len(i))
        min_len = min(lens)
        res = ''
        for j in range(min_len):
            if strs[0][j] != strs[-1][j]:
                return res
            else:
                res += strs[0][j]
        return res 

# 20. Valid Parentheses

class Solution20:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                l.append(i)
            else:
                if not len(l):
                    return False
                u = l.pop(-1)
                if (i==')' and u=='(') or (i==']' and u=='[') or (i=='}' and u=='{'):
                    continue
                else:
                    return False
        if len(l):
            return False
        else:
            return True

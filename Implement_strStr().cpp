// Must have the exception of haystack.length()<needle.length() situation
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") return 0;
        int i, j;
        if (haystack.length()<needle.length()) return -1;
        for (i=0;i<haystack.length()-needle.length()+1;i++){
            for (j=0;j<needle.length();j++){
                if (haystack[i+j] != needle[j]) break;
            }
            if (j==needle.length()) return i;
        }
        return -1;
    }
};

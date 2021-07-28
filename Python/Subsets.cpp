class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res{{}};
        for (int i=0; i<nums.size(); i++){
            int m = int(res.size());
            for (int j=0; j<m; j++){
                vector n = res[j];
                n.push_back(nums[i]);
                res.push_back(n);
            }
        }
        return res;
    }
};

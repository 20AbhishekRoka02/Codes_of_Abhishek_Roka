 /* 
 
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
 
 Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 
 T.C -> O(n)
 S.C -> O(n)

*/

 vector<int> twoSum(vector<int>& nums, int target) {
    
     unordered_map<int , int>m;
        vector<int>ans;     
        for(int i = 0;i<nums.size();i++){
            
            int t = target - nums[i];
            
            if(m.find(t) != m.end()){
                ans.push_back(nums[m[t]]);
                ans.push_back( nums[i]);
                return ans;
            }
            m[nums[i]] = i;
        }
        return ans;
    }

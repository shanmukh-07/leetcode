class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long int s = 0;
        long long int c = 0;
        for(int i=0;i<nums.size();i++){
            if (nums[i] == 0){
                c+=1;
                s+=c;
            }else{
                c=0;
            }
        }
        return s;
    }
};
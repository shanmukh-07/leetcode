class Solution {
public:
    long long maximumHappinessSum(vector<int>& h, int k) {
        long long int n = h.size();
        sort(h.rbegin(),h.rend());
        long long int c = k;
        long long int sum = 0;
        for(int i=0;i<k;i++){
            long long int tv = h[i]-(k-c);
            if(tv>0){
                sum += tv;
            }
            c--;
        }
        return sum;
    }
};

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happy, int k) {
        sort(happy.begin(), happy.end(), greater<int>());
        long long r = 0;
        for (int i = 0; i < k; ++i) {
            r += max(0, happy[i] - i);
        }
        return r;
    }
};
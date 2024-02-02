class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int>v;
        for(int i=1;i<10;i++){
            int n = i;
            int nn = i+1;
            while(n <= high && nn <= 9){
                n = n*10 + nn;
                if(n >= low && n <= high){
                    v.push_back(n);
                }
                nn++;
            }
        }
        sort(v.begin(),v.end());
        return v;
    }
};

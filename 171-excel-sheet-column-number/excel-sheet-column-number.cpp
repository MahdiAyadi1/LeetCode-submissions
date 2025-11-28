class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char index:columnTitle)
            result = (int(index) - 64) + result * 26 ;
        return result;
    }
};
class Solution {
public:
    int lengthOfLastWord(string s) {
        while (s.ends_with(" ")) {
            s = s.substr(0,s.length()-1);
        }
        return s.length() - s.find_last_of(" ") - 1 ;
    }
};
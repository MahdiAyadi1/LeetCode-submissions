class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        std::string prefix = strs[0];
        for (std::string word: strs) {
            if (prefix.length() > word.length()) {
                prefix = prefix.substr(0, word.length());
            }
            for (int index = 0; index < prefix.length(); index++) {
                if (prefix[index] != word[index]) {
                    prefix = prefix.substr(0, index);
                    break;
                }
            }
            if (prefix.length() == 0) {
                return "";
            }
        }
        return prefix;
    }
};
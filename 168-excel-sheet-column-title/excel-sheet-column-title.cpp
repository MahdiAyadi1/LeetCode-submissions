class Solution {
public:
    string convertToTitle(int columnNumber) {
        
        string result = "";
        while (columnNumber > 26){
            columnNumber--;
            result =(char(65 + columnNumber % 26))+result;
            columnNumber = columnNumber / 26;
        }
        result =(char(64 + columnNumber))+result;
        return result;
    }
};
class Solution {
    public int scoreOfString(String s) {
        int sum = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            int tmpValue = s.charAt(i) - s.charAt(i+1);
            tmpValue = tmpValue < 0 ? -tmpValue : tmpValue;
            sum += tmpValue;
        }      
        return sum;
    }
}

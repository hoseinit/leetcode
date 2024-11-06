class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        int result = 0;
        for(char ch:jewels.toCharArray()) {
            String tmp = stones;
            while (tmp.indexOf(ch) >= 0) {
                tmp = tmp.substring(tmp.indexOf(ch) + 1);
                result ++;
            }
        }
        return result;       
    }
}

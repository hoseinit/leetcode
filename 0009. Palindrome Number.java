// Easy solution by converting to String and reversing it
class Solution {
    public boolean isPalindrome(int x) {

        String value = String.valueOf(x);
        String reverseValue = new StringBuffer(value).reverse().toString();
        return value.equals(reverseValue) ? true : false;
    }
}

// Hard solution by avoiding the String conversion
class Solution {
    public boolean isPalindrome(int x) {

        if (x < 0 || (x > 0 && x % 10 == 0)) {
            return false;
        }

        int y = 0;
        while (y < x) {
            y = y * 10 + x % 10;
            x /= 10;
        }
        
        return x == y || x == y / 10;
    }
}


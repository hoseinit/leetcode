// Easy solution with switch

class Solution {
    public int romanToInt(String s) {

        int sum = 0;
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            
            switch(c) {
                case 'I':
                    if (i+1 < s.length() && (s.charAt(i+1) == 'V' || s.charAt(i+1) == 'X')) {
                        sum -= 1;
                    } else {
                        sum += 1;
                    }    
                    break;
                case 'V':
                    sum += 5;
                    break;
                case 'X':
                    if (i+1 < s.length() && (s.charAt(i+1) == 'L' || s.charAt(i+1) == 'C')) {
                        sum -= 10;
                    } else {
                        sum += 10;
                    } 
                    break;
                case 'L':
                    sum += 50;
                    break;
                case 'C':
                        if (i+1 < s.length() && (s.charAt(i+1) == 'D' || s.charAt(i+1) == 'M')) {
                            sum -= 100;
                        } else {
                            sum += 100;
                        } 
                    break;
                case 'D':
                    sum += 500;
                    break;
                case 'M':
                    sum += 1000;
                    break;
            }

        }
        return sum;
    }
}

// Cleaner solution with Hashmap
class Solution {
    public int romanToInt(String s) {

        int sum = 0;

        Map<Character, Integer> m = new HashMap();

        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);


        for (int i=0; i<s.length(); i++) {
            if(i < s.length() - 1 && (m.get(s.charAt(i+1)) > m.get(s.charAt(i)))) {
                sum -= m.get(s.charAt(i));
            } else {
                sum += m.get(s.charAt(i));
            }
        }
        return sum;
    }
}

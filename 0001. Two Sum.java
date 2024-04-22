// Easy solution but has O(n^2)
class Solution {
    public int[] twoSum(int[] nums, int target) {

        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if(nums[i] + nums[j] == target)
                    return new int[]{i,j};
            }
        }
        return new int[0];
    }
}

// Using HashMap which has O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for(int i=0; i<nums.length; i++) {
                int x = nums[i];
                int y = target - x;
                if (numMap.containsKey(y)) {
                    return new int[]{numMap.get(y), i};
                }
                numMap.put(x, i);
        }
        return new int[0];
    }
}

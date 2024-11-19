class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> array = new HashSet<>();
        for(int i = 0; i<nums.length; i++) {
            if (!array.add(nums[i])) {
                return true;
            }
        }
            return false;
    }
}
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hash = new HashMap<>();
        for(int i=0; i<nums.length;i++) {
            hash.put(nums[i],i);
        }
        
        for(int i=0; i<nums.length;i++) {
            int search = target-nums[i];
            if(hash.containsKey(search) && hash.get(search) != i) {
                return new int[]{i,hash.get(search)};
            }
        }
        return null;
    }
}

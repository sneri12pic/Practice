class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int j = 0;
        for(int i = j+1; i < nums.length && j < nums.length; i++){
            System.out.printf("%d %d\n", j, i);
            if(nums[j] + nums[i] == target){
                result[0] = j;
                result[1] = i;
                return result;
            }
            else if(i == nums.length - 1){
                j++;
                i = j;
            }
        }
        return result;
    }
}

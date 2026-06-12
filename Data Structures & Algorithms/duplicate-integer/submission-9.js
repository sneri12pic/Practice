class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let length = nums.length
        let map = new Map();
        for(let i = 0; i < length; i++){  
            if(map.has(nums[i])){
                return true
            }
            map.set(nums[i], true)
        }
        return false
    }
}

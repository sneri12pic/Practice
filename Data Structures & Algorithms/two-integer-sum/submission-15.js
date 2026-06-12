class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let i = 0;
        let j = 1;
        let map = new Map();
        for(let x = 0; x < nums.length; x++){
            map.set(nums[x], x);
        }
        console.log(map);
        
        for(;i < nums.length; i++){
            let complement = target - nums[i];

            if (map.has(complement) && map.get(complement) !== i) {
                return [i, map.get(complement)];
            }
        }

    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        // We dont need to follow specif order and since the result IS DISTINCT we should use hashMap

        // Count frequencies
        for (int num: nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Output most frequent elements
        List<Integer>[] buckets = new List[nums.length+1];
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            
            int value = e.getKey();      // the original number
            int count = e.getValue();    // its frequency

            /* Create a bucket for a new nubmer e.g. -> if the number 6 appears 3 times bucket[count : 3]
                and add a value to it (buckets[3] : null, buckets[3] = new ArrayList) -> buckets[3].add(6); 
            */ 
            if(buckets[count] == null) buckets[count] = new ArrayList<>();
            buckets[count].add(value);
        }

        int[] result = new int[k];
        int idx = 0;

        // Go from Highest freq to lowest
        for (int count = buckets.length - 1; count >= 0 && idx < k; count--) {
            if (buckets[count] != null) {
                for (int num : buckets[count]) {
                    result[idx++] = num;
                    if (idx == k) break;
                }
            }
        }
        return result;
    }
}

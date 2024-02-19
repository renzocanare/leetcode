import java.util.HashMap;
import java.util.Scanner;
import java.util.Map;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (nMap.containsKey(complement)) {
                return new int[] {nMap.get(complement), i};
            } else {
                nMap.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}

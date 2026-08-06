public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();
        
        for (var i = 0; i < nums.Length; i++)
        {
            if (dict.ContainsKey(target - nums[i]))
                return new int[] { dict[target - nums[i]], i };
            else
                dict.Add(nums[i], i);
        }
        return new int[] { -1, -1 };
    }
}

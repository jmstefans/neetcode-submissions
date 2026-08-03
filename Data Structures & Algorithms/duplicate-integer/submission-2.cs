public class Solution {
    public bool hasDuplicate(int[] nums) {
        var hashmap = new HashSet<int>();
        for (var i = 0; i < nums.Length; i++)
        {
            if (hashmap.Contains(nums[i]))
                return true;
            else
                hashmap.Add(nums[i]);
        }
        return false;
    }
}
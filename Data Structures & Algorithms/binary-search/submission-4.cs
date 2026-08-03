public class Solution
{
    public int Search(int[] nums, int target)
    {
        var l = 0;
        var r = nums.Length - 1;

        while (l <= r)
        {
            var m = (l + r) / 2;  // need floor here I think

            if (nums[m] < target)
            {
                l = m + 1;
            }
            else if (nums[m] > target)
            {
                r = m - 1;
            }
            else
            {
                return m;
            }
        }

        return -1;
    }
}
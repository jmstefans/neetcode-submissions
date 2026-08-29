public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // just divide the total product by each element O(2n) reducing to O(n)
        // var product = 1;

        // for (var i = 0; i < nums.Length; i++)
        // {
        //     product *= nums[i];
        // }

        // var result = new int[nums.Length];

        // for (var i = 0; i < nums.Length; i++)
        // {
        //     result[i] = product / nums[i];
        // }

        // 2nd harder approach you could calculate the prefix product and the postfix products for O(n) I believe
        var prefixProducts = new int[nums.Length]; // first element doesn't have a prefix so just put a 1
        var postfixProducts = new int[nums.Length]; // last element doesn't have a postfix so just put a 1

        var workingProduct = 1;

        // fill out prefix product array
        for (var i = 0; i < nums.Length; i++)
        {
            if (i == 0)
                prefixProducts[i] = 1;
            else
            {
                prefixProducts[i] = nums[i - 1] * workingProduct;
                workingProduct = prefixProducts[i];
            }
        }
        
        // reset workingProduct variable
        workingProduct = 1;

        // fill out prefix product array
        for (var i = nums.Length - 1; i >= 0; i--)
        {
            if (i == nums.Length - 1)
                postfixProducts[i] = 1;
            else
            {
                postfixProducts[i] = nums[i + 1] * workingProduct;
                workingProduct = postfixProducts[i];
            }
        }

        // fill out result array
        var result = new int[nums.Length];

        for (var i = 0; i < nums.Length; i++)
        {
            result[i] = prefixProducts[i] * postfixProducts[i];
        }

        return result;
    }
}

public class Solution {
    public int MaxArea(int[] heights) {
        /*
            brute force is too slow
            maybe we can use two pointers to go through the array once and just move the pointers intelligently?
            left pointer on the left and right pointer on the right
            then shift whichever pointer is lower height and if equal shift left
            keep going until left pointer is not less than right pointer
        */
        
        var max = 0;
        var l = 0;
        var r = heights.Length - 1;

        // Keep going until we've gone through the list
        while (l < r)     
        {
            // compute current container max and if greater than our max, update max
            var distance = r - l;
            var height = Math.Min(heights[l], heights[r]);
            var curConArea = distance * height;
            if (curConArea > max)
                max = curConArea;

            // Update pointer(s)
            if (heights[l] > heights[r])
                r--;
            else
                l++;
        }   

        return max;
        
        /*       
            start with brute force
            use 2 pointers to form all possible containers
            containers aren't valid if there is a value that is greater than or equal to one of the pointers/edges so skip those
            water height is only going to be as tall as the minimum of the two pointers/edges
        

        var max = 0;

        for (var i = 0; i < heights.Length; i++)
        {
            for (var j = i + 1; j < heights.Length; j++)
            {
                // check if valid container (no heigher bars between pointers)
                // 
            }
        }
        */
    }
}

public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {




        // iterate through adding to hashset value to frequency
        // then need to go through values and return the top most frequent somehow
        // could sort but that would be nlogn
        // maybe just have a datastructure as we go that keeps the top k frequent ones

        var dict = new Dictionary<int, int>(); // number and it's frequency
        for (var i = 0; i < nums.Length; i++)
        {
            if (!dict.ContainsKey(nums[i]))
                dict[nums[i]] = 1;
            else
                dict[nums[i]]++;
        }


        List<int>[] bucketArray = new List<int>[nums.Length + 1]; // index is the count or frequency and value is a list of ints that occur that many times
        foreach (var kvp in dict)
        {
            int frequency = kvp.Value;
            if (bucketArray[frequency] == null)
                bucketArray[frequency] = new List<int>();

            bucketArray[frequency].Add(kvp.Key);
        }

        var j = nums.Length;
        var result = new List<int>();
        while (j >= 0 && result.Count < k)
        {
            if (bucketArray[j] != null)
            {
                foreach (int num in bucketArray[j])
                {
                    result.Add(num);
                    if (result.Count == k)
                        break;
                }
            }
            j--;
        }

        return result.ToArray();
    }
}

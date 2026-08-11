public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs)
    {
        var groups = new Dictionary<string, List<string>>();

        foreach (string s in strs)
        {
            var count = new int[26]; // frequency of characters array of length 26 for each lowercase alphabetic character
            foreach (char c in s)
                count[c - 'a']++;

            // create unique string key for this anagram
            string key = String.Join(',', count);

            // if not in our groups add an empty list
            if (!groups.ContainsKey(key))
                groups[key] = new List<string>();

            // always add this "anagram key" to the groups
            groups[key].Add(s);
        }

        return groups.Values.ToList();






        // var result = new List<List<string>>();

        // // Iterate through each of the strings one at a time
        // for (var i = 0; i < strs.Length; i++)
        // {
        //     // Create a Dictionary or array of the current string with each key 
        //     // being the letter like "a" in "act" (constraint says all lowercase)
        //     // and the value being the number of times it occurs so "1".


        //     // See if this dictionary is in our list of dictionaries.

        //     // If it's in there than add this word to that list.

        //     // Otherwise create a new list


            
        // }

        // return result;
    }
}

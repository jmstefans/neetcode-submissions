public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;

        var sDict = new Dictionary<char, int>();
        var tDict = new Dictionary<char, int>();

        foreach (var character in s)
        {
            if (sDict.ContainsKey(character))
                sDict[character]++;
            else
                sDict[character] = 1;
        }

        foreach (var character in t)
        {
            if (tDict.ContainsKey(character))
                tDict[character]++;
            else
                tDict[character] = 1;
        }

        return sDict.Count == tDict.Count && sDict.All(kvp => tDict.TryGetValue(kvp.Key, out var val) && EqualityComparer<int>.Default.Equals(kvp.Value, val));
    }
}

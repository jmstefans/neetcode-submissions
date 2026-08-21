public class Solution {

    public string Encode(IList<string> strs) {
        string result = "";
        foreach (string s in strs)
        {
            result += s.Length + "#" + s;
        }
        return result;
    }

    public List<string> Decode(string s) {
        var result = new List<string>();
        if (string.IsNullOrEmpty(s))
            return result;

        var i = 0;
        while (i < s.Length)
        {
            int delimiterIndex = s.IndexOf("#", i);
            int length = int.Parse(s.Substring(i, delimiterIndex - i));
            string cur = s.Substring(delimiterIndex + 1, length);
            result.Add(cur);
            i = delimiterIndex + length + 1;
        }
        return result;
   }
}

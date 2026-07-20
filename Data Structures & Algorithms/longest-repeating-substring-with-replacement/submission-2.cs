public class Solution {
    public int CharacterReplacement(string s, int k) 
    {
        // Frequency of each uppercase letter in the current window.
        // Index 0 = 'A', 1 = 'B', ..., 25 = 'Z'
        int[] characterCounts = new int[26];

        // Left edge of the sliding window
        int left = 0;

        // Highest frequency of any single character in the current window
        int maxCharacterFrequency = 0;

        // Best answer found so far
        int longestWindow = 0;

        // Expand the window one character at a time
        for (int right = 0; right < s.Length; right++)
        {
            // Convert the current character into an array index.
            //
            // Example:
            // 'A' - 'A' = 0
            // 'B' - 'A' = 1
            // 'C' - 'A' = 2
            int currentCharacterIndex = s[right] - 'A';

            // We've added this character to our window, so increase its count.
            characterCounts[currentCharacterIndex]++;

            // If this character is now the most common character in the window,
            // update our maximum frequency.
            maxCharacterFrequency = Math.Max(
                maxCharacterFrequency,
                characterCounts[currentCharacterIndex]);

            // Current window size
            int windowSize = right - left + 1;

            // If we'd need more than k replacements to make every character
            // in this window the same, shrink the window from the left.
            //
            // The cheapest way to make every character in the window the same is to
            // keep the character that already appears the most.
            //
            // Replacements needed = windowSize - maxCharacterFrequency
            //
            // If that exceeds k, this window is no longer valid.
            while (windowSize - maxCharacterFrequency > k)
            {
                // Remove the leftmost character from the window.
                int leftCharacterIndex = s[left] - 'A';
                characterCounts[leftCharacterIndex]--;

                // Move the left edge of the window right by one.
                left++;

                // Recalculate the window size after shrinking.
                windowSize = right - left + 1;
            }

            // Update our best answer if this valid window is the largest so far.
            longestWindow = Math.Max(longestWindow, windowSize);
        }

        return longestWindow;
    









        // // go through left to right 0 and 1
        // // go through right to left 

        // // Base case of string length 1
        // if (s.Length == 1)
        //     return 1;

        // // doesn't take into account starting characters
        
        // // left to right
        // var l = 0;
        // var r = 1;
        // var tempK = k;
        // var max = 1;
        // var tempMax = 1;

        // while (r < s.Length)
        // {
        //     char c = s[l];
        //     if (s[r] == c) // encountered the same character so no substitution needed, just increase max
        //     {
        //         tempMax++;
        //         r++;
        //     }
        //     else if (tempK > 0) // substitution available so pretend we did it
        //     {                
        //         tempMax++;
        //         r++;
        //         tempK--;
        //     }
        //     else
        //     {
        //         // no more substitutions and we aren't repeating the character so we're done for this window so update max
        //         if (tempMax > max)
        //             max = tempMax;

        //         // reset the sliding window to the next character over (might be able to be smarter and move l further to the right)
        //         l++;
        //         r = l + 1;
        //         tempK = k;
        //         tempMax = 1;
        //     }
        // }
        
        // // hit the end of the string so potentially update max
        // if (tempMax > max)
        //     max = tempMax;

        // // right to left 
        // r = s.Length - 1;
        // l = r - 1;
        // tempK = k;
        // tempMax = 1;

        // while (l >= 0)
        // {
        //     char c = s[r];
        //     if (s[l] == c) // encountered the same character so no substitution needed, just increase max
        //     {
        //         tempMax++;
        //         l--;
        //     }
        //     else if (tempK > 0) // substitution available so pretend we did it
        //     {                
        //         tempMax++;
        //         l--;
        //         tempK--;
        //     }
        //     else
        //     {
        //         // no more substitutions and we aren't repeating the character so we're done for this window so update max
        //         if (tempMax > max)
        //             max = tempMax;

        //         // reset the sliding window to the next character over (might be able to be smarter and move l further to the right)
        //         r--;
        //         l = r - 1;
        //         tempK = k;
        //         tempMax = 1;
        //     }
        // }
        
        // // hit the end of the string so potentially update max
        // if (tempMax > max)
        //     max = tempMax;

        // // return max
        // return max;
    }
}

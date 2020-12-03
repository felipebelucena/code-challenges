class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, return the length of the longest substring of s such that
        the frequency of each character in this substring is greater than or equal to k.

        Example 1:

        Input: s = "aaabb", k = 3
        Output: 3
        Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

        Example 2:

        Input: s = "ababbc", k = 2
        Output: 5
        Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

        Constraints:

        - 1 <= s.length <= 104
        - s consists of only lowercase English letters.
        - 1 <= k <= 105

        https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3544/
        """
        stringLength = len(s)

        if stringLength < k:
            return 0

        lettersMap = self.buildLettersMap(s, k)

        # find first non valid letter index
        midPoint = -1
        for i in range(stringLength):
            if lettersMap[s[i]] < k:
                midPoint = i
                break
        else:
            # no invalid letter found, return the string length as the answer
            return stringLength

        return max(self.longestSubstring(s[:midPoint], k), self.longestSubstring(s[midPoint + 1:], k))

    def buildLettersMap(self, s, k):
        lettersMap = {}
        for letter in s:
            lettersMap[letter] = lettersMap.setdefault(letter, 0) + 1
        return lettersMap


if __name__ == '__main__':
    s = Solution()

    assert s.longestSubstring("aaabb", 3) == 3
    assert s.longestSubstring("ababbc", 2) == 5
    assert s.longestSubstring("a", 1) == 1
    assert s.longestSubstring("ababacb", 3) == 0

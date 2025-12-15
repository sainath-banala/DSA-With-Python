"""
Docstring for Arrays.Easy.valid_anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # my approach
        # checking whether both the strings are of same length
        if len(s) != len(t):
            return False
        else:
            # creating two dictionaries to store the count of each element in both the strings
            str1_map = {}
            str2_map = {}
            for i in range(len(s)):
                # first string
                if s[i] in str1_map:
                    str1_map[s[i]] += 1
                else:
                    str1_map[s[i]] = 1
                
                # second string
                if t[i] in str2_map:
                    str2_map[t[i]] += 1
                else:
                    str2_map[t[i]] = 1

            for i in str1_map:
                if (str1_map.get(i) is None or str2_map.get(i) is None) or (str1_map.get(i) != str2_map.get(i)):
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    str1, str2 = map(str, input("Enter the two words separated by space: ").strip().split(" "))
    print(solution.isAnagram(str1, str2))
    
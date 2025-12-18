"""
Docstring for Arrays.Medium.group_anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""
import copy

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

    def groupAnagrams_my_approach(self, strs: list[str]) -> list[list[str]]:
        length_of_list = len(strs)
        if length_of_list == 0:
            return []
        elif length_of_list == 1:
            return [strs]

        temp_list = copy.deepcopy(strs)
        output_list = []
        for i in range(length_of_list):
            string = strs[i]
            if string in temp_list:
                current_anagram_list = [string]
                for j in range(i+1, length_of_list):
                    string2 = strs[j]
                    if self.isAnagram(string, string2):
                        current_anagram_list.append(string2)
                        if temp_list.count(string2) > 1:
                            temp_list.remove(string2)
                            temp_list.remove(string2)
                        elif string2 in temp_list:
                            temp_list.remove(string2)
                        # print(f"temp_list: {temp_list}")
                        # print(f"current_list: {current_anagram_list}")
                output_list.append(current_anagram_list)
            # print(f"output_lsit: {output_list}")
        
        # print(output_list)
        return output_list
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # dictionary to store all unique strings with same combination(since Anagrams have common property → Sorted string is the SAME)
        anagram_map = {}
        # iterating through each string in the list
        for string in strs:
            # initalizing a list to store the count of each alphabet in the string at that respective character position
            char_cnt_in_string = [0] * 26
            # getting the character count of each element 
            for character in string:
                # Assuming only lowercase a-z
                index = ord(character) - ord('a')
                # incrementing the count of a specific character at that specific alphabet location Ex: if the character is d, we will update index 3 to 1
                char_cnt_in_string[index] += 1
            
            # since list is not hashable, it can't be kept as key in dictionary(as it will raise error: TypeError: unhashable type: 'list')
            # that's why we are converting the list to tuple which is immutable
            key = tuple(char_cnt_in_string)
            
            # checking if the same key that is the words with same character count already exists in the dictionary
            if key in anagram_map:
                anagram_map[key].append(string)
            else:
                anagram_map[key] = [string]

        return list(anagram_map.values())


if __name__ == '__main__':
    solution = Solution()
    list_of_strings = list(map(str, input("Enter the words separated by space: ").strip().split(" ")))
    list_of_strings = ["rag","orr","err","bad","foe","ivy","tho","gem","len","cat","ron","ump","nev","cam","pen","dis","rob","tex","sin","col","buy","say","big","wed","eco","bet","fog","buy","san","kid","lox","sen","ani","mac","eta","wis","pot","sid","dot","ham","gay","oar","sid","had","paw","sod","sop"]
    print(solution.groupAnagrams(list_of_strings))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        for word in strs:
            anagram_key = ''.join(sorted(word))
            if anagram_key in anagrams_dict:
                anagrams_dict[anagram_key] = anagrams_dict[anagram_key] + [word]
            else:
                anagrams_dict[anagram_key] = [word]

        # anagrams_dict = {"abt": ["bat"], "ant": ["nat","tan"], "aet": ["ate","eat","tea"], "aett": ["teat"]}

        return list(anagrams_dict.values()) # [["bat"], ["nat","tan"], ["ate","eat","tea"], ["teat"]]
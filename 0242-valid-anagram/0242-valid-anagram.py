class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = list(s)
        uniq_s_chars = set(list(s))
        s_char_freq = {}
        for char in uniq_s_chars:
            count = s_chars.count(char)
            s_char_freq[char] = count

        
        t_chars = list(t)
        uniq_t_chars = set(list(t))
        t_char_freq = {}
        for char in uniq_t_chars:
            count = t_chars.count(char)
            t_char_freq[char] = count

        sorted_s = {k: v for k, v in sorted(s_char_freq.items(), key=lambda item: item[1])}
        sorted_t = {k: v for k, v in sorted(t_char_freq.items(), key=lambda item: item[1])}

        return sorted_s == sorted_t
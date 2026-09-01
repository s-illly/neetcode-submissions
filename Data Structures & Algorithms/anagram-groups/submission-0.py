class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            anagram = "".join(sorted(i))
            if anagram in d:
                d[anagram].append(i)
            else:
                d[anagram] = []
                d[anagram].append(i)
        return list(d.values())


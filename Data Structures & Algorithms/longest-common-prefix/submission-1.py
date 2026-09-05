class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        IDX = 0
        smallest = min([len(s) for s in strs])
        while IDX < smallest:
            c = strs[0][IDX]
            for s in strs[1:]:
                if s[IDX] == c:
                    pass
                else:
                    return strs[0][0:IDX]
            IDX += 1
        return strs[0][0:IDX]
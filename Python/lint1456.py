class Solution:
    """
    @param target: the target string
    @param words: words array
    @return: whether the target can be matched or not
    """

    def matchFunction(self, target, words):
        def solve(tt, ws):
            if not tt: return True
            for i in xrange(len(ws)):
                if tt[0] in ws[i]:
                    if solve(tt[1:], ws[:i]+ws[i+1:]):
                        return True
            return False

        if len(target) > len(words): return False
        return solve(target, words)

print Solution().matchFunction("oznpdrcd",
["zsadchwmmkuvh","rsnpqojnlwfmkvzch","xgqk","ppmqpceairhdontpwfxl","wfirlgbdevjdbdrgq","qo","pvwdmc","ctdcsw","cfafyv"])
print Solution().matchFunction("ally",["buy","discard","lip","yep"])
print Solution().matchFunction("ray",["buy","discard","lip","rep"])
class Solution:
    def groupAnagrams(self, strs):
        ana = {}
        for s in strs:
            key = str(sorted(s))

            if key in ana:
                ana[key] += [s]
            else:
                ana[key] = [s]

        return ana.values()

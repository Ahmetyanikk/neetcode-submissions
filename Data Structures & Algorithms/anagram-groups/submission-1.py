class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= {}

        for Str in strs:
            key = "".join(sorted(Str))

            if key in groups:
                groups[key].append(Str)
            
            else:
                groups[key] = [Str]

        return list(groups.values())
        
        
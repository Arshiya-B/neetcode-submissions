class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in data:
                data[key] = []
            
            data[key].append(s)

        return list(data.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dir={}
        for s in strs:
            key="".join(sorted(s))
            if key not in dir:
                dir[key]=[]
            dir[key].append(s)
        return list(dir.values())
        
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if same characters and length
        #if i in s is in t, put them in a set or seperate list
        #return boolean so 
        compare = []
        contrast = []
        for i in s:
            compare.append(i)
        for j in t:
            contrast.append(j)
        
        if sorted(compare) == sorted(contrast):
            return True
        else:
            return False
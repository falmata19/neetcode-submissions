class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if same characters and length
        #if i in s is in t, put them in a set or seperate list
        #return boolean so 
        holder = []
        another = []
        for i in s:
            holder.append(i)
        for j in t:
            another.append(j)

        if sorted(holder) == sorted(another):
            return True
        else:
            return False
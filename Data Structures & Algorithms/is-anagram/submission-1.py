class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for letter in s :
              occ=0
              if letter not in  d1.keys():
                occ+=1
                d1[letter]=occ
              else:
                 d1[letter]=d1[letter]+1

        for letter in t :
             occ=0
             if letter not in  d2.keys():
                occ+=1
                d2[letter]=occ
             else:
                 d2[letter]=d2[letter]+1

        if d1==d2:
            return True 
        else:
            return False

        
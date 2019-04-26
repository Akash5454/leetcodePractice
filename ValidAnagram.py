# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:42:16 2019

@author: akash
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        dict1 = dict.fromkeys(list('qwertyuiopasdfghjklzxcvbnm'),0)
        dict2 = dict.fromkeys(list('qwertyuiopasdfghjklzxcvbnm'),0)
        for i in range(len(s)):
            dict1[s[i]] += 1
            dict2[t[i]] += 1
        return(dict1 == dict2)